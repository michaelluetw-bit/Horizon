"""Email service for handling subscriptions and sending summaries."""

import email
import html
import imaplib
import logging
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr
from typing import List

try:
    import markdown
except ImportError:
    markdown = None

from ..ai.markdown_utils import clean_app_summary_markdown
from ..models import EmailConfig

_EMAIL_RE = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")

_NO_REPLY_PATTERNS = re.compile(
    r"(noreply|no-reply|donotreply|do-not-reply|mailer-daemon|postmaster|nobody|"
    r"automated|automaton|bounce|returns|noreponse)",
    re.IGNORECASE,
)

_MAX_SUBSCRIBERS = 500

logger = logging.getLogger(__name__)


def _is_valid_subscriber_email(addr: str) -> bool:
    """Validate that an email address is a real subscriber (not automated)."""
    if not _EMAIL_RE.match(addr):
        return False
    if _NO_REPLY_PATTERNS.search(addr):
        return False
    return True


class EmailManager:
    """Manages email subscriptions and sending summaries."""

    def __init__(self, config: EmailConfig, console=None):
        self.config = config
        self.pwd = os.getenv(self.config.password_env)
        if console is None:
            try:
                from rich.console import Console

                self.console = Console()
            except ImportError:

                class DummyConsole:
                    def print(self, *args, **kwargs):
                        print(*args, **kwargs)

                self.console = DummyConsole()
        else:
            self.console = console

        if not self.pwd and self.config.enabled:
            logger.warning(
                f"Environment variable {self.config.password_env} not set. Email features may fail."
            )
            self.console.print(
                f"[yellow]Warning: Environment variable {self.config.password_env} not set. Email features may fail.[/yellow]"
            )

    def check_subscriptions(self, storage_manager):
        """Checks inbox for subscription requests and updates subscriber list."""
        if not self.config.enabled or not self.config.imap_enabled:
            return

        try:
            mail = imaplib.IMAP4_SSL(self.config.imap_server, self.config.imap_port)
            mail.login(self.config.email_address, self.pwd)
            mail.select("INBOX")

            subscribers = storage_manager.load_subscribers()

            for email_addr in self._collect_request_senders(mail, self.config.subscribe_keyword):
                if len(subscribers) >= _MAX_SUBSCRIBERS:
                    logger.warning(
                        "Max subscriber limit (%d) reached, skipping %s",
                        _MAX_SUBSCRIBERS, email_addr,
                    )
                    continue
                if email_addr not in subscribers:
                    storage_manager.add_subscriber(email_addr)
                    subscribers = storage_manager.load_subscribers()
                    self._send_reply(
                        email_addr,
                        "Subscribed to Horizon",
                        "You have been successfully subscribed to Horizon daily summaries.",
                    )
                    logger.info(f"Added subscriber: {email_addr}")
                else:
                    logger.info(f"Already subscribed: {email_addr}")

            for email_addr in self._collect_request_senders(mail, self.config.unsubscribe_keyword):
                if email_addr in subscribers:
                    storage_manager.remove_subscriber(email_addr)
                    subscribers = storage_manager.load_subscribers()
                    self._send_reply(
                        email_addr,
                        "Unsubscribed from Horizon",
                        "You have been successfully unsubscribed from Horizon daily summaries.",
                    )
                    logger.info(f"Removed subscriber: {email_addr}")
                else:
                    logger.info(f"Not subscribed: {email_addr}")

            mail.close()
            mail.logout()

        except Exception as e:
            logger.error(f"Error checking subscriptions: {e}")

    @staticmethod
    def _collect_request_senders(mail, keyword: str) -> List[str]:
        """Return validated sender addresses of unseen mails whose subject equals *keyword*."""
        safe_keyword = keyword.replace("\\", "\\\\").replace('"', '\\"')
        status, messages = mail.search(None, f'(UNSEEN SUBJECT "{safe_keyword}")')
        if status != "OK" or not messages[0]:
            return []

        addresses: List[str] = []
        for e_id in messages[0].split():
            _, msg_data = mail.fetch(e_id, "(RFC822)")
            for response_part in msg_data:
                if not isinstance(response_part, tuple):
                    continue
                msg = email.message_from_bytes(response_part[1])

                subject = str(msg.get("Subject") or "").strip()
                if subject.upper() != keyword.upper():
                    continue

                sender = msg.get("From")
                if not sender:
                    continue
                _, email_addr = parseaddr(sender)
                if email_addr and _is_valid_subscriber_email(email_addr):
                    addresses.append(email_addr)
        return addresses

    def send_daily_summary(self, summary_md: str, subject: str, subscribers: List[str]):
        """Sends the daily summary to all subscribers."""
        if not self.config.enabled or not subscribers:
            return

        cleaned_summary = clean_app_summary_markdown(summary_md)
        safe_summary = html.escape(cleaned_summary)
        # html.escape protects against HTML injection from scraped content,
        # but it also mangles Markdown blockquote markers at line starts;
        # restore those so quotes still render.
        safe_summary = re.sub(r"(?m)^([ \t]*)&gt; ", r"\1> ", safe_summary)
        html_content = (
            markdown.markdown(safe_summary)
            if markdown
            else f"<pre>{safe_summary}</pre>"
        )

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                code {{ background-color: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}
                pre {{ background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
                blockquote {{ border-left: 4px solid #ddd; padding-left: 15px; color: #777; }}
                .footer {{ margin-top: 40px; font-size: 12px; color: #888; text-align: center; border-top: 1px solid #eee; padding-top: 20px; }}
            </style>
        </head>
        <body>
            {html_content}
            <div class="footer">
                <p>Sent by {self.config.sender_name}</p>
                <p>To unsubscribe, please reply with "{self.config.unsubscribe_keyword}"</p>
            </div>
        </body>
        </html>
        """

        try:
            with smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(
                    self.config.smtp_username or self.config.email_address, self.pwd
                )

                for subscriber in subscribers:
                    msg = MIMEMultipart("alternative")
                    msg["Subject"] = subject
                    msg["From"] = (
                        f"{self.config.sender_name} <{self.config.email_address}>"
                    )
                    msg["To"] = subscriber

                    text_part = MIMEText(cleaned_summary, "plain")
                    html_part = MIMEText(html_body, "html")

                    msg.attach(text_part)
                    msg.attach(html_part)

                    try:
                        server.send_message(msg)
                        logger.info(f"Sent summary to {subscriber}")
                    except Exception as e:
                        logger.error(f"Failed to send to {subscriber}: {e}")

        except Exception as e:
            logger.error(f"SMTP Error: {e}")

    def _send_reply(self, to_email: str, subject: str, body: str):
        """Helper to send a simple reply."""
        try:
            with smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(
                    self.config.smtp_username or self.config.email_address, self.pwd
                )

                msg = MIMEText(body)
                msg["Subject"] = subject
                msg["From"] = f"{self.config.sender_name} <{self.config.email_address}>"
                msg["To"] = to_email

                server.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to send reply to {to_email}: {e}")
