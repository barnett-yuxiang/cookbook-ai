import pytest

from task1 import md5_hash


def test_md5_hash_empty_string():
    assert md5_hash("") == "d41d8cd98f00b204e9800998ecf8427e"


def test_md5_hash_simple_string():
    assert md5_hash("hello") == "5d41402abc4b2a76b9719d911017c592"


def test_md5_hash_longer_string():
    assert (
        md5_hash("The quick brown fox jumps over the lazy dog")
        == "9e107d9d372bb6826bd81d3542a419d6"
    )


def test_md5_hash_special_characters():
    assert md5_hash("!@#$%^&*()_+") == "d751713988987e9331980363e24189ce"
