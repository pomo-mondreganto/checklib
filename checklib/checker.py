import checklib.assertions
import checklib.http
import checklib.status


class CheckFinished(Exception):
    pass


class BaseChecker(checklib.assertions.CheckerAssertionsMixin, checklib.http.CheckerHttpHelpersMixin):
    obj = None

    def __init__(self, host):
        self.host = host
        self.status = checklib.status.Status.OK.value
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
        raise NotImplementedError('You must implement this method')

    def put(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def get(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def cquit(self, status, public='', private=None):
        if private is None:
            private = public

        self.status = status.value
        self.public = public
        self.private = private

        raise self.get_check_finished_exception()
