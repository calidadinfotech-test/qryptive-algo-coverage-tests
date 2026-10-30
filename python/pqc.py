"""Post-quantum schemes that are NOT ML-KEM / ML-DSA / SLH-DSA, including broken ones."""
import oqs
from pyhsslms import HssLmsPrivateKey


def firmware_signing_key():
    return HssLmsPrivateKey.genkey("qa-firmware-key", levels=2)


def code_kem_bike():
    return oqs.KeyEncapsulation("BIKE-L1")


def lattice_kem_saber():
    return oqs.KeyEncapsulation("LightSaber-KEM")


def multivariate_mayo():
    return oqs.Signature("MAYO-2")


def multivariate_uov():
    return oqs.Signature("OV-Is")


def code_signature_cross():
    return oqs.Signature("cross-rsdp-128-balanced")


def isogeny_signature():
    return oqs.Signature("SQIsign-lvl1")


def lattice_signature_hawk():
    return oqs.Signature("HAWK-512")


def broken_isogeny_kem():
    return oqs.KeyEncapsulation("SIKE-p434")


def broken_multivariate_signature():
    return oqs.Signature("Rainbow-I-Classic")


def broken_hfe_signature():
    return oqs.Signature("GeMSS128")


def withdrawn_zk_signature():
    return oqs.Signature("picnic3_L1")
