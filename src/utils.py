import re


def str_to_int(value: str) -> int:
    return re.sub("[^A-Za-z0-9]+", "", value)
