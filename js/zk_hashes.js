const { buildPoseidon, buildMimc7, buildPedersenHash } = require('circomlibjs');
const { keccak256, toUtf8Bytes } = require('ethers');
const groestlLib = require('groestl-hash-js');

async function commitmentHash(a, b) {
  const hasher = await buildPoseidon();
  return hasher.F.toString(hasher([a, b]));
}

async function circuitHash(x, k) {
  const hasher = await buildMimc7();
  return hasher.F.toString(hasher.hash(x, k));
}

async function pointHash(bytes) {
  const hasher = await buildPedersenHash();
  return hasher.hash(bytes);
}

function eventTopic(signature) {
  return keccak256(toUtf8Bytes(signature));
}

function coinHash(buffer) {
  return groestlLib.groestl_2(buffer, 1, 1);
}

module.exports = { commitmentHash, circuitHash, pointHash, eventTopic, coinHash };
