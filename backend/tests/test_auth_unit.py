import pytest
from app.core.security import (
    validate_password_strength,
    get_password_hash,
    verify_password,
    create_access_token,
    decode_access_token,
    generate_refresh_token,
    hash_token,
)
from app.core.exceptions import UnauthorizedException


def test_password_strength():
    # Valid password
    valid, err = validate_password_strength("Nam@123456")
    assert valid is True
    assert err is None

    # Too short
    valid, err = validate_password_strength("Nam@1")
    assert valid is False

    # No uppercase
    valid, err = validate_password_strength("nam@123456")
    assert valid is False

    # No digit
    valid, err = validate_password_strength("Nam@abcdef")
    assert valid is False

    # No special char
    valid, err = validate_password_strength("Nam1234567")
    assert valid is False


def test_password_hashing():
    pw = "SuperSecret@123"
    hashed = get_password_hash(pw)
    assert hashed != pw
    assert verify_password(pw, hashed) is True
    assert verify_password("WrongPassword@123", hashed) is False


def test_access_token():
    user_id = "user-1234"
    email = "user@test.com"
    roles = ["Author"]

    token = create_access_token(user_id=user_id, email=email, roles=roles)
    assert isinstance(token, str)

    payload = decode_access_token(token)
    assert payload["sub"] == user_id
    assert payload["email"] == email
    assert payload["roles"] == roles


def test_refresh_token_generation():
    raw_token, token_hash, expires_at = generate_refresh_token()
    assert len(raw_token) > 20
    assert len(token_hash) == 64
    assert hash_token(raw_token) == token_hash
