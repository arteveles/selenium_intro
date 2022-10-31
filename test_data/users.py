import random

_user = [
    ("123test@gmail.com", "password"),
    ("user", "bitnami"),
    ("admin", "bitnami1")
]


def get_user():
    return random.choice(_user)


def get_valid_user():
    return _user[1]


def get_invalid_user():
    return _user[2]


def login_user():
    return _user[0]
