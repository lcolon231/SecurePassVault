import random
import string


def generate_password(length=16):
    """
    This generates a random password with a mix of letters, digits, and punctuation.
    The default length is 16 characters
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
