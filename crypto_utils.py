from cryptography.fernet import Fernet
import os


def save_key(filename):
    """
    It generates and save a Fernet encryption key to a file.
    """

    key = Fernet.generate_key()
    with open(filename,"wb") as f:
        f.write(key)


def load_key(filename):
    """
    Loads the Fernet encryption key from a file
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Key file '{filename}' not found.")
    with open(filename, "rb") as f:
        key = f.read().strip()
    if not key:
        raise ValueError(f"Key file '{filename}' is empty or corrupted.")
    return key



def encrypt_data(data, key):
    """
    Encrypts a string using the provided Fernet key
    """

    f = Fernet(key)
    return f.encrypt(data.encode())


def decrypt_data(data, key):
    """
    Decrypts data using the provided Fernet key.
    """

    f = Fernet(key)
    return f.decrypt(data).decode()
