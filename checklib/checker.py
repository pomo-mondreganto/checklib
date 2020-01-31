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

    def action(self, action, *args, **kwargs):
        if action == 'check':
            return self.check(*args, **kwargs)
        elif action == 'put':
            return self.put(*args, **kwargs)
        else:
            return self.get(*args, **kwargs)

    def check(self, *_args, **_kwargs):
        raise NotImplemented

    def put(self, *_args, **_kwargs):
        raise NotImplemented

    def get(self, *_args, **_kwargs):
        raise NotImplemented

    def cquit(self, status, public='', private=None):
        if private is None:
            private = public

        self.status = status
        self.public = public
        self.private = private

        raise self.get_check_finished_exception()
