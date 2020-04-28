import os
import secrets
import string

import requests

import checklib.internal as internal

with open(internal.get_resource_path('usernames.txt')) as f:
    usernames_db = f.read().split('\n')

with open(internal.get_resource_path('useragents.txt')) as f:
    useragents_db = f.read().split('\n')


def rnd_bytes(length):
    return os.urandom(length)


def rnd_string(length, alphabet=None):
    if alphabet is None:
        alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def rnd_username(salt=5):
    return secrets.choice(usernames_db) + rnd_string(salt)


def rnd_password(l=20):
    return rnd_string(l)


def rnd_useragent():
    return secrets.choice(useragents_db)


def get_initialized_session():
    sess = requests.Session()
    sess.headers['User-Agent'] = rnd_useragent()
    return sess
