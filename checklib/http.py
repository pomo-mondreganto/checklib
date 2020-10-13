import json

import requests

import checklib.status
import checklib.utils as utils


def get_json(r: requests.Response, public: str, status=checklib.status.Status.MUMBLE):
    try:
        data = r.json()
    except (UnicodeDecodeError, json.decoder.JSONDecodeError):
        utils.cquit(status, public, f'Invalid json on {r.url}')
    else:
        return data


def get_text(r: requests.Response, public: str, status=checklib.status.Status.MUMBLE) -> str:
    try:
        data = r.text
    except UnicodeDecodeError:
        utils.cquit(status, public, f'Unable to decode text from {r.url}')
    else:
        return data


def check_response(r: requests.Response, public: str, status=checklib.status.Status.MUMBLE):
    if r.status_code >= 500:
        utils.cquit(checklib.status.Status.DOWN, public, f'Code {r.status_code} on {r.url}')
    if not r.ok:
        utils.cquit(status, public, f'Error on {r.url}: {r.status_code}')


class CheckerHttpHelpersMixin:
    def get_json(self, r: requests.Response, public: str, status=checklib.status.Status.MUMBLE):
        json_errors = (
            UnicodeDecodeError,
            json.decoder.JSONDecodeError,
            ValueError,
        )
        try:
            data = r.json()
        except json_errors:
            self.cquit(status, public, f'Invalid json on {r.url}')
        else:
            return data

    def get_text(self, r: requests.Response, public: str, status=checklib.status.Status.MUMBLE) -> str:
        try:
            data = r.text
        except UnicodeDecodeError:
            self.cquit(status, public, f'Unable to decode text from {r.url}')
        else:
            return data

    def check_response(self, r: requests.Response, public: str, status=checklib.status.Status.MUMBLE):
        if r.status_code >= 500:
            self.cquit(checklib.status.Status.DOWN, public, f'Code {r.status_code} on {r.url}')
        if not r.ok:
            self.cquit(status, public, f'Error on {r.url}: {r.status_code}')

    def cquit(self, *_args, **_kwargs):
        raise NotImplementedError
