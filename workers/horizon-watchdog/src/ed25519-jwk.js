export function compatibleEd25519Jwk(key) {
  if (key?.kty === "OKP" && key.crv === "Ed25519" && key.alg === "Ed25519") {
    return { ...key, alg: "EdDSA" };
  }
  return key;
}
