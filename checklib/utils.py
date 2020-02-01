import sys
from contextlib import contextmanager

import checklib


def cquit(status, public='', private=None):
    if private is None:
        private = public

    print(public, file=sys.stdout)
    print(private, file=sys.stderr)
    assert (type(status) == checklib.status.Status)
    sys.exit(status.value)


@contextmanager
def handle_exception(exc, public, private, status=checklib.status.Status.MUMBLE):
    try:
        yield True
    except SystemError:
        raise
    except exc:
        cquit(status, public, private)
    except Exception:
        raise
