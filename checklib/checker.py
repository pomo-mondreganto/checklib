import json
import typing

import requests

import checklib.assertions
import checklib.generators
import checklib.http
import checklib.status


class CheckFinished(Exception):
    pass


class BaseChecker(checklib.assertions.CheckerAssertionsMixin, checklib.http.CheckerHttpHelpersMixin):
    gets_count: int = 1
    puts_count: int = 1
    vulns: int = 1
    timeout: int = 10
    uses_attack_data: bool = False

    def __init__(self, host: str):
        self.host: str = host
        self.status: str = checklib.status.Status.OK.value
        self.public: str = ''
        self.private: str = ''
        self._sessions: typing.List[requests.Session] = []

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
        data = {
            'gets': self.gets_count,
            'puts': self.puts_count,
            'vulns': self.vulns,
            'timeout': self.timeout,
            'attack_data': self.uses_attack_data,
        }
        self.cquit(checklib.status.Status.OK, json.dumps(data))

    def check(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def put(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def get(self, *_args, **_kwargs):
        raise NotImplementedError('You must implement this method')

    def get_initialized_session(self) -> requests.Session:
        sess = checklib.generators.get_initialized_session()
        self._sessions.append(sess)
        return sess

    def cquit(self, status: checklib.status.Status, public: str = '', private: typing.Optional[str] = None):
        if private is None:
            private = public

        self.status = status.value
        self.public = public
        self.private = private

        for sess in self._sessions:
            sess.close()
        self._sessions = []

        raise self.get_check_finished_exception()
