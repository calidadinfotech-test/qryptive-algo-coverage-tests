import { XWing } from '@noble/post-quantum/hybrid.js';
import { schnorr } from '@noble/curves/secp256k1';
import { bls12_381 } from '@noble/curves/bls12-381';

export function makeHybridKeys(seed: Uint8Array) {
  return XWing.keygen(seed);
}

export function signTaprootMessage(msg: Uint8Array, priv: Uint8Array): Uint8Array {
  return schnorr.sign(msg, priv);
}

export function signValidatorMessage(msg: Uint8Array, priv: Uint8Array): Uint8Array {
  return bls12_381.sign(msg, priv);
}
