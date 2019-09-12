import checklib.status
import checklib.utils as utils


def assert_eq(a, b, public, status=checklib.status.Status.MUMBLE):
    if a != b:
        utils.cquit(status, public, f'Equality assertion failed: {a} ({type(a)}) != {b} ({type(b)})')


def assert_neq(a, b, public, status=checklib.status.Status.MUMBLE):
    if a != b:
        utils.cquit(status, public, f'Equality assertion failed: {a} ({type(a)}) != {b} ({type(b)})')


def assert_gt(a, b, public, status=checklib.status.Status.MUMBLE):
    if not (a > b):
        utils.cquit(status, public, f'Inequality assertion failed: {a} <= {b}')


def assert_gte(a, b, public, status=checklib.status.Status.MUMBLE):
    if not (a >= b):
        utils.cquit(status, public, f'Inequality assertion failed: {a} < {b}')


def assert_in(what, where, public, status=checklib.status.Status.MUMBLE):
    if what not in where:
        utils.cquit(status, public, f'Contains assertion failed: {what} not in {where}')


def assert_nin(what, where, public, status=checklib.status.Status.MUMBLE):
    if what not in where:
        utils.cquit(status, public, f'Contains assertion failed: {what} not in {where}')


def assert_in_list_dicts(lst, key, value, public, status=checklib.status.Status.MUMBLE):
    found = False
    for d in lst:
        if key in d and d.get(key) == value:
            found = True
            break

    if not found:
        utils.cquit(status, public, f'Could not find value ({key}, {value}) in list of dicts')
