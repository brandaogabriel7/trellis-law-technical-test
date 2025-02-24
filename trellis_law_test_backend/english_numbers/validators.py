def validate_integer(value: str) -> None:
    try:
        int(value)
    except ValueError:
        raise ValueError("Value is not a valid integer")