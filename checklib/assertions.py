import checklib.status
import checklib.utils as utils


def assert_eq(a, b, public: str, status=checklib.status.Status.MUMBLE):
    if a != b:
        utils.cquit(status, public, f'Equality assertion failed: {a} ({type(a)}) != {b} ({type(b)})')


def assert_neq(a, b, public: str, status=checklib.status.Status.MUMBLE):
    if a == b:
        utils.cquit(status, public, f'Inequality assertion failed: {a} ({type(a)}) != {b} ({type(b)})')


def assert_gt(a, b, public: str, status=checklib.status.Status.MUMBLE):
    if not (a > b):
        utils.cquit(status, public, f'Inequality assertion failed: {a} <= {b}')


def assert_gte(a, b, public: str, status=checklib.status.Status.MUMBLE):
    if not (a >= b):
        utils.cquit(status, public, f'Inequality assertion failed: {a} < {b}')


def assert_in(what, where, public: str, status=checklib.status.Status.MUMBLE):
    if what not in where:
        utils.cquit(status, public, f'Contains assertion failed: {what} not in {where}')


def assert_nin(what, where, public: str, status=checklib.status.Status.MUMBLE):
    if what in where:
        utils.cquit(status, public, f'Not contains assertion failed: {what} not in {where}')


def assert_in_list_dicts(lst, key, value, public: str, status=checklib.status.Status.MUMBLE):
    found = False
    for d in lst:
        if key in d and d.get(key) == value:
            found = True
            break

    if not found:
        utils.cquit(status, public, f'Could not find value ({key}, {value}) in list of dicts')


class CheckerAssertionsMixin:
    def assert_eq(self, a, b, public: str, status=checklib.status.Status.MUMBLE):
        if a != b:
            self.cquit(status, public, f'Equality assertion failed: {a} ({type(a)}) != {b} ({type(b)})')

    def assert_neq(self, a, b, public: str, status=checklib.status.Status.MUMBLE):
        if a == b:
            self.cquit(status, public, f'Inequality assertion failed: {a} ({type(a)}) != {b} ({type(b)})')

    def assert_gt(self, a, b, public: str, status=checklib.status.Status.MUMBLE):
        if not (a > b):
            self.cquit(status, public, f'Inequality assertion failed: {a} <= {b}')

    def assert_gte(self, a, b, public: str, status=checklib.status.Status.MUMBLE):
        if not (a >= b):
            self.cquit(status, public, f'Inequality assertion failed: {a} < {b}')

    def assert_in(self, what, where, public: str, status=checklib.status.Status.MUMBLE):
        if what not in where:
            self.cquit(status, public, f'Contains assertion failed: {what} not in {where}')

    def assert_nin(self, what, where, public: str, status=checklib.status.Status.MUMBLE):
        if what in where:
            self.cquit(status, public, f'Not contains assertion failed: {what} not in {where}')

    def assert_in_list_dicts(self, lst, key, value, public: str, status=checklib.status.Status.MUMBLE):
        found = False
        for d in lst:
            if key in d and d.get(key) == value:
                found = True
                break

        if not found:
            self.cquit(status, public, f'Could not find value ({key}, {value}) in list of dicts')

    def cquit(self, *_args, **_kwargs):
        raise NotImplementedError
