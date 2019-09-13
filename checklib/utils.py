import sys
from contextlib import contextmanager

import checklib.status


def cquit(code, public='', private=None):
    if private is None:
        private = public

    print(public, file=sys.stdout)
    print(private, file=sys.stderr)
    assert (type(code) == checklib.status.Status)
    sys.exit(code.value)


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
