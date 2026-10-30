const { SignJWT, CompactEncrypt } = require('jose');
const nodeCrypto = require('node:crypto');

async function signTicket(payload, privateKey) {
  return new SignJWT(payload).setProtectedHeader({ alg: 'ES256K' }).sign(privateKey);
}

async function sealTicket(plaintext, kek) {
  return new CompactEncrypt(plaintext).setProtectedHeader({ alg: 'A256KW', enc: 'A256GCM' }).encrypt(kek);
}

async function newSigningKey() {
  return nodeCrypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify']);
}

module.exports = { signTicket, sealTicket, newSigningKey };
