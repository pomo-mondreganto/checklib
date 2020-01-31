import sys
from contextlib import contextmanager

import checklib


def cquit(status, public='', private=None, *args, **kwargs):
    if private is None:
        private = public

    if checklib.checker.BaseChecker.obj is not None:
        return checklib.checker.BaseChecker.obj.cquit(
            status=status,
            public=public,
            private=private,
            *args, **kwargs,
        )

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
