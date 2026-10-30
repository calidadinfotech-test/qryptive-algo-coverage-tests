"""Block ciphers, lightweight ciphers and AEAD modes that are less common."""
from Crypto.Cipher import AES, CAST
from cryptography.hazmat.primitives.ciphers.aead import AESGCMSIV, AESOCB3, AESSIV
from pygost.gost3412 import GOST3412Kuznechik, GOST3412Magma
from pygost.gost28147 import ecb_encrypt as legacy_block_encrypt
from speck import SpeckCipher
from simon import SimonCipher
from pypresent import Present
import ascon


def seal_siv(key: bytes, data: bytes):
    cipher = AES.new(key, AES.MODE_SIV)
    return cipher.encrypt_and_digest(data)


def seal_ocb(key: bytes, nonce: bytes, data: bytes):
    cipher = AES.new(key, AES.MODE_OCB, nonce=nonce)
    return cipher.encrypt_and_digest(data)


def seal_gcm_siv(key: bytes, nonce: bytes, data: bytes, aad: bytes) -> bytes:
    return AESGCMSIV(key).encrypt(nonce, data, aad)


def seal_ocb3(key: bytes, nonce: bytes, data: bytes) -> bytes:
    return AESOCB3(key).encrypt(nonce, data, None)


def seal_deterministic(key: bytes, data: bytes, aad: bytes) -> bytes:
    return AESSIV(key).encrypt(data, [aad])


def legacy_cast(key: bytes, iv: bytes, data: bytes) -> bytes:
    return CAST.new(key, CAST.MODE_CBC, iv).encrypt(data)


def gost_block(key: bytes, block: bytes) -> bytes:
    return GOST3412Kuznechik(key).encrypt(block)


def gost_small_block(key: bytes, block: bytes) -> bytes:
    return GOST3412Magma(key).encrypt(block)


def gost_legacy(key: bytes, data: bytes) -> bytes:
    return legacy_block_encrypt(key, data)


def iot_speck(key: int, plaintext: int) -> int:
    return SpeckCipher(key, key_size=128, block_size=128).encrypt(plaintext)


def iot_simon(key: int, plaintext: int) -> int:
    return SimonCipher(key, key_size=128, block_size=128).encrypt(plaintext)


def rfid_block(key: bytes, block: bytes) -> bytes:
    return Present(key).encrypt(block)


def lightweight_seal(key: bytes, nonce: bytes, ad: bytes, pt: bytes) -> bytes:
    return ascon.ascon_encrypt(key, nonce, ad, pt, variant="Ascon-128")
