import os


def get_resource_path(resource: str) -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'resources', resource)
