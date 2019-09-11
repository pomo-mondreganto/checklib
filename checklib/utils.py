import sys

import checklib.status as status


def cquit(code, public='', private=None):
    if private is None:
        private = public

    print(public, file=sys.stdout)
    print(private, file=sys.stderr)
    assert (type(code) == status.Status)
    sys.exit(code.value)
