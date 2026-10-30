"""Ordinary code that only LOOKS like cryptography. A correct scanner reports nothing here."""
import random
import json

# TODO: migrate RSA-2048 signing to ML-DSA-65 and replace SHA-1 with SHA-256
# cipher = DES.new(key, DES.MODE_ECB)

random.seed(42)
IDEA_BOARD = ["present", "cross", "rainbow", "magma", "tiger"]
TEA_TYPES = ["green", "black", "oolong"]
bike_count = 3
saber_length_cm = 90
hawk_sightings = 2
lms_course_url = "https://lms.example.com/course/42"
cross_join_sql = "SELECT * FROM a CROSS JOIN b"
greeting = "Simon says: keep the seed packets dry"
aesthetic_theme = "dark"


class PresentationLayer:
    """Formats reports. Mentions of SHA-256 or BLS in a docstring are not usage."""

    def present(self, rows):
        return json.dumps({"rows": rows, "theme": aesthetic_theme})


def opaque_color(alpha: float) -> str:
    return f"rgba(0, 0, 0, {alpha})"


def bls_labour_statistics_url(series: str) -> str:
    return "https://www.bls.gov/data/" + series
