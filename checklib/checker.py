import checklib.assertions
import checklib.generators
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
        self._sessions = []

    @staticmethod
    def get_check_finished_exception():
        return CheckFinished

    def action(self, action, *args, **kwargs):
        if action == 'info':
            return self.info(*args, **kwargs)
        elif action == 'check':
            return self.check(*args, **kwargs)
        elif action == 'put':
            return self.put(*args, **kwargs)
        elif action == 'get':
            return self.get(*args, **kwargs)
        else:
            self.cquit(checklib.status.Status.ERROR, 'Checker failed', f'Invalid action: {action}')

    def info(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def check(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def put(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def get(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def get_initialized_session(self):
        sess = checklib.generators.get_initialized_session()
        self._sessions.append(sess)
        return sess

    def cquit(self, status, public='', private=None):
        if private is None:
            private = public

        self.status = status.value
        self.public = public
        self.private = private

        for sess in self._sessions:
            sess.close()
        self._sessions = []

        raise self.get_check_finished_exception()
