"""Key derivation, password hashing and password-authenticated key exchange."""
import crypt
import bcrypt
import srp
import opaque
from spake2 import SPAKE2_A
from balloon import balloon_hash
from passlib.hash import md5_crypt, sha512_crypt
from Crypto.Protocol.KDF import PBKDF1
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.kbkdf import KBKDFHMAC, CounterLocation, Mode
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from cryptography.hazmat.primitives.kdf.x963kdf import X963KDF


def counter_mode_kdf(key: bytes) -> bytes:
    kdf = KBKDFHMAC(algorithm=hashes.SHA256(), mode=Mode.CounterMode, length=32, rlen=4, llen=4,
                    location=CounterLocation.BeforeFixed, label=b"qa", context=b"ctx", fixed=None)
    return kdf.derive(key)


def concat_kdf(shared: bytes) -> bytes:
    return ConcatKDFHash(algorithm=hashes.SHA256(), length=32, otherinfo=b"qa").derive(shared)


def ansi_kdf(shared: bytes) -> bytes:
    return X963KDF(algorithm=hashes.SHA256(), length=32, sharedinfo=b"qa").derive(shared)


def legacy_pbkdf(password: bytes, salt: bytes) -> bytes:
    return PBKDF1(password, salt, 16, count=1000)


def openssh_key_kdf(password: bytes, salt: bytes) -> bytes:
    return bcrypt.kdf(password=password, salt=salt, desired_key_bytes=32, rounds=100)


def linux_shadow_hash(password: str) -> str:
    return crypt.crypt(password, "$y$j9T$F5Jx5fExrKuPp53xLKQ..1$")


def legacy_shadow_hash(password: str) -> str:
    return md5_crypt.hash(password)


def modern_shadow_hash(password: str) -> str:
    return sha512_crypt.using(rounds=656000).hash(password)


def memory_hard_hash(password: bytes, salt: bytes) -> bytes:
    return balloon_hash(password, salt)


def register_user(username: bytes, password: bytes):
    return srp.create_salted_verification_key(username, password)


def register_opaque(password: bytes, server_sk: bytes, ids):
    return opaque.Register(password, server_sk, ids)


def start_pairing(code: bytes) -> bytes:
    return SPAKE2_A(code).start()
