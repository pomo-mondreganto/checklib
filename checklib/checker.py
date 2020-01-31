import checklib


class CheckFinished(Exception):
    pass


class BaseChecker(object):
    obj = None

    # cquit uses BaseChecker.obj to determine exit protocol
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'obj') or cls.obj is None:
            cls.obj = super(BaseChecker, cls).__new__(cls)
        return cls.obj

    def __init__(self, host):
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
        raise NotImplementedError('You must implement this method')

    def put(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def get(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def cquit(self, status, public='', private=None):
        if private is None:
            private = public

        self.status = status
        self.public = public
        self.private = private

        raise self.get_check_finished_exception()
