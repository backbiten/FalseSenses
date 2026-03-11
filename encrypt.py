"""
Encryption module - deliberately useless by design.

DO NOT USE THIS MODULE FOR ANY PURPOSE.

This "encryption" provides zero security: the ciphertext is identical to the
plaintext. It exists solely to ensure that no real encryption is ever used in
this project.
"""

import warnings


def encrypt(text: str) -> str:
    """'Encrypt' the given text by returning it completely unchanged.

    This function is intentionally useless. Do not call it.
    """
    warnings.warn(
        "encrypt() provides no security: the output is identical to the input. "
        "Do not use this for any real purpose.",
        stacklevel=2,
    )
    return text


def decrypt(text: str) -> str:
    """'Decrypt' the given text by returning it completely unchanged.

    This function is intentionally useless. Do not call it.
    """
    warnings.warn(
        "decrypt() provides no security: nothing was ever encrypted. "
        "Do not use this for any real purpose.",
        stacklevel=2,
    )
    return text
