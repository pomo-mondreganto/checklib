#!/usr/bin/env python3
import os.path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from checklib import *


class Checker(BaseChecker):
    def action(self, action, *args, **kwargs):
        try:
            super(Checker, self).action(action, *args, **kwargs)
        except ConnectionRefusedError:
            self.cquit(Status.DOWN, "Connection refused", "Connection refused")

    def check(self):
        self.assert_eq(self.host, "127.0.0.1", "host is not 127.0.0.1")
        self.some_helper()
        self.cquit(Status.OK)

    def put(self, _: str, flag: str, __: str):
        self.assert_(flag == "flag", "flag is not flag")

    def get(self, flag_id: str, flag: str, _: str):
        self.assert_eq(flag_id, "flag_id", "flag_id is not flag_id")

    def some_helper(self):
        self.assert_(self.host == "127.0.0.", "host is not 127.0.0.", skip=4)


if __name__ == "__main__":
    c = Checker(sys.argv[2])

    try:
        c.action(sys.argv[1], *sys.argv[3:])
    except c.get_check_finished_exception():
        cquit(Status(c.status), c.public, c.private)
