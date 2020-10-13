import sys
import typing
from contextlib import contextmanager

import checklib


def cquit(status: checklib.status.Status, public: str = '', private: typing.Optional[str] = None):
    if private is None:
        private = public

    print(public, file=sys.stdout)
    print(private, file=sys.stderr)
    assert (type(status) == checklib.status.Status)
    sys.exit(status.value)


@contextmanager
def handle_exception(exc, public: str, private: str, status: checklib.status.Status = checklib.status.Status.MUMBLE):
    try:
        yield True
    except SystemError:
        raise
    except exc:
        cquit(status, public, private)
    except Exception:
        raise
