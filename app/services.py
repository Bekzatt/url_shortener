"""
Утилита для генерации коротких идентификаторов.
"""

import hashlib

def generate_short_id(url: str) -> str:
    """
    Генерирует короткий идентификатор по URL с использованием SHA-256.
    """
    return hashlib.sha256(str(url).encode()).hexdigest()[:8]
