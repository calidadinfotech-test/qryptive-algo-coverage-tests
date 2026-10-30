"""Hash functions and XOFs outside the SHA-2 / SHA-3 / BLAKE2 set."""
import hashlib
from Crypto.Hash import keccak, TupleHash128, cSHAKE128, KangarooTwelve as K12
from cryptography.hazmat.primitives import hashes
from pygost.gost34112012256 import GOST34112012256
import botan3


def ethereum_address_hash(public_key: bytes) -> str:
    return keccak.new(digest_bits=256, data=public_key).hexdigest()


def truncated_sha2(data: bytes) -> bytes:
    h = hashes.Hash(hashes.SHA512_256())
    h.update(data)
    return h.finalize()


def short_truncated_sha2(data: bytes) -> str:
    return hashlib.new("sha512_224", data).hexdigest()


def customised_xof(data: bytes) -> bytes:
    return cSHAKE128.new(data=data, custom=b"QA").read(32)


def structured_hash(parts):
    h = TupleHash128.new(digest_bytes=32)
    for p in parts:
        h.update(p)
    return h.digest()


def fast_xof(data: bytes) -> bytes:
    return K12.new(data=data, custom=b"").read(32)


def gost_digest(data: bytes) -> bytes:
    return GOST34112012256(data).digest()


def legacy_tiger(data: bytes) -> bytes:
    h = botan3.HashFunction("Tiger")
    h.update(data)
    return h.final()
