import warnings

import pytest

from encrypt import decrypt, encrypt


def test_encrypt_returns_plaintext_unchanged():
    with pytest.warns(UserWarning):
        assert encrypt("hello") == "hello"


def test_decrypt_returns_ciphertext_unchanged():
    with pytest.warns(UserWarning):
        assert decrypt("hello") == "hello"


def test_encrypt_equals_decrypt():
    text = "super secret message"
    with pytest.warns(UserWarning):
        encrypted = encrypt(text)
    with pytest.warns(UserWarning):
        decrypted = decrypt(text)
    assert encrypted == decrypted == text


def test_encryption_provides_no_security():
    plaintext = "password123"
    with pytest.warns(UserWarning, match="no security"):
        assert encrypt(plaintext) == plaintext, "Encryption must be completely useless"

