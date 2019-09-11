import json

import checklib.status
import checklib.utils as utils


def get_json(r, public, status=checklib.status.Status.MUMBLE):
    try:
        data = r.json()
    except (UnicodeDecodeError, json.decoder.JSONDecodeError):
        utils.cquit(status, public, f'Invalid json on {r.url}')
    else:
        return data


def get_text(r, public, status=checklib.status.Status.MUMBLE):
    try:
        data = r.text
    except UnicodeDecodeError:
        utils.cquit(status, public, f'Invalid json on {r.url}')
    else:
        return data


def check_response(r, public):
    if r.status_code >= 500:
        utils.cquit(checklib.status.Status.DOWN, public, f'Code {r.status_code} on {r.url}')
    if not r.ok:
        utils.cquit(checklib.status.Status.MUMBLE, public, f'Error on {r.url}: {r.status_code}')
