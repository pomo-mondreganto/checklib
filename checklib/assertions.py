from checklib.status import Status
import checklib.utils as utils
import checklib.internal as internal


def __cquit_helper(status: Status, public: str, private: str, skip=3):
    caller_info = internal.caller_info(skip=skip)
    utils.cquit(status, public, f"[{caller_info}] {private}")


def assert_(expr: bool, public: str, status=Status.MUMBLE):
    if not expr:
        __cquit_helper(status, public, "assertion failed")


def assert_eq(a, b, public: str, status=Status.MUMBLE):
    if a != b:
        __cquit_helper(
            status,
            public,
            f"equality assertion failed: {a} ({type(a)}) != {b} ({type(b)})",
        )


def assert_neq(a, b, public: str, status=Status.MUMBLE):
    if a == b:
        __cquit_helper(
            status,
            public,
            f"inequality assertion failed: {a} ({type(a)}) != {b} ({type(b)})",
        )


def assert_gt(a, b, public: str, status=Status.MUMBLE):
    if not (a > b):
        __cquit_helper(
            status,
            public,
            f"inequality assertion failed: {a} <= {b}",
        )


def assert_gte(a, b, public: str, status=Status.MUMBLE):
    if not (a >= b):
        __cquit_helper(
            status,
            public,
            f"inequality assertion failed: {a} < {b}",
        )


def assert_in(what, where, public: str, status=Status.MUMBLE):
    if what not in where:
        __cquit_helper(
            status, public, f"contains assertion failed: {what} not in {where}"
        )


def assert_nin(what, where, public: str, status=Status.MUMBLE):
    if what in where:
        __cquit_helper(
            status, public, f"not contains assertion failed: {what} not in {where}"
        )


def assert_in_list_dicts(lst, key, value, public: str, status=Status.MUMBLE):
    found = False
    for d in lst:
        if key in d and d.get(key) == value:
            found = True
            break

    if not found:
        __cquit_helper(
            status, public, f"could not find value ({key}, {value}) in list of dicts"
        )


class CheckerAssertionsMixin:
    def assert_(self, expr: bool, public: str, status=Status.MUMBLE, skip=3):
        if not expr:
            self.__cquit_helper(status, public, "assertion failed", skip=skip)

    def assert_eq(self, a, b, public: str, status=Status.MUMBLE, skip=3):
        if a != b:
            self.__cquit_helper(
                status,
                public,
                f"equality assertion failed: {a} ({type(a)}) != {b} ({type(b)})",
                skip=skip,
            )

    def assert_neq(self, a, b, public: str, status=Status.MUMBLE, skip=3):
        if a == b:
            self.__cquit_helper(
                status,
                public,
                f"inequality assertion failed: {a} ({type(a)}) != {b} ({type(b)})",
                skip=skip,
            )

    def assert_gt(self, a, b, public: str, status=Status.MUMBLE, skip=3):
        if not (a > b):
            self.__cquit_helper(
                status, public, f"inequality assertion failed: {a} <= {b}", skip=skip
            )

    def assert_gte(self, a, b, public: str, status=Status.MUMBLE, skip=3):
        if not (a >= b):
            self.__cquit_helper(
                status, public, f"inequality assertion failed: {a} < {b}", skip=skip
            )

    def assert_in(self, what, where, public: str, status=Status.MUMBLE, skip=3):
        if what not in where:
            self.__cquit_helper(
                status,
                public,
                f"contains assertion failed: {what} not in {where}",
                skip=skip,
            )

    def assert_nin(self, what, where, public: str, status=Status.MUMBLE, skip=3):
        if what in where:
            self.__cquit_helper(
                status,
                public,
                f"not contains assertion failed: {what} not in {where}",
                skip=skip,
            )

    def assert_in_list_dicts(
        self, lst, key, value, public: str, status=Status.MUMBLE, skip=3
    ):
        found = False
        for d in lst:
            if key in d and d.get(key) == value:
                found = True
                break

        if not found:
            self.__cquit_helper(
                status,
                public,
                f"could not find value ({key}, {value}) in list of dicts",
                skip=skip,
            )

    def __cquit_helper(self, status: Status, public: str, private: str, skip=3):
        caller_info = internal.caller_info(skip=skip)
        self.cquit(status, public, f"[{caller_info}] {private}")

    def cquit(self, *_args, **_kwargs):
        raise NotImplementedError
