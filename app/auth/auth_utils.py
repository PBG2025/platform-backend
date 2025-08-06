# app/auth/auth_utils.py
# (Stub for password hashing, OAuth, etc.)

def hash_password(password):
    return "hashed-" + password


def verify_password(plain, hashed):
    return hashed == "hashed-" + plain

