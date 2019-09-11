import os


def get_resource_path(resource):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'resources', resource)
