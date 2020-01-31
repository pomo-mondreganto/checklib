import requests
import checklib


class CheckFinished(Exception):
    pass


class Checker:
    def __init__(self, host):
        checklib.cquit = self.cquit
        self.host = host
        self.status = checklib.Status.OK
        self.public = ''
        self.private = ''

    @staticmethod
    def get_check_finished_exception():
        return CheckFinished

    def action(self, action, *_args, **_kwargs):
        try:
            if action == 'check':
                return self.check()
            elif action == 'put':
                return self.put()
            else:
                return self.get()
        except requests.exceptions.ConnectionError:
            self.cquit(checklib.Status.DOWN, 'Connection error', 'Got requests connection error')

    def check(self):
        raise NotImplemented

    def put(self):
        raise NotImplemented

    def get(self):
        raise NotImplemented

    def cquit(self, status, public='', private=None):
        if private is None:
            private = public

        self.status = status
        self.public = public
        self.private = private

        raise self.get_check_finished_exception()
