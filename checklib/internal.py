import dataclasses
import inspect
import os
from typing import Optional


def get_resource_path(resource: str) -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "resources", resource)


@dataclasses.dataclass
class CallerInfo:
    package: Optional[str]
    module: Optional[str]
    klass: Optional[str]
    caller: Optional[str]
    line: int

    def __iter__(self):
        yield self.package
        yield self.module
        yield self.klass
        yield self.caller
        yield self.line

    def __str__(self):
        res = ".".join(
            str(x) for x in self.__iter__() if x is not None and not isinstance(x, int)
        )
        return f"{res}:{self.line}"


def caller_info(skip=2) -> Optional[CallerInfo]:
    stack = inspect.stack()
    start = 0 + skip
    if len(stack) < start + 1:
        return None

    parentframe = stack[start][0]

    module_info = inspect.getmodule(parentframe)
    module = None
    package = None
    if module_info:
        mod = module_info.__name__.split(".")
        if len(mod) > 1:
            package = mod[0]
            module = mod[1]
        else:
            module = mod[0]

    klass = None
    if "self" in parentframe.f_locals:
        klass = parentframe.f_locals["self"].__class__.__name__

    caller = None
    if parentframe.f_code.co_name != "<module>":  # top level usually
        caller = parentframe.f_code.co_name

    line = parentframe.f_lineno

    del parentframe

    return CallerInfo(package, module, klass, caller, line)
