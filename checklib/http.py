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
