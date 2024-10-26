# calcute md5 hash of a string
import hashlib

def md5_hash(string: str) -> str:
    return hashlib.md5(string.encode).hexdigest()
