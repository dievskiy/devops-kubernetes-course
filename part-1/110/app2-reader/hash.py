import uuid


def generate_random_string() -> str:
    """
    Generates random string
    """
    return str(uuid.uuid4())
