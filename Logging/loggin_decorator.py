"""Logging functunality"""
from functools import wraps
import functools
from typing import Any, Callable

import logging


# Basic logging config
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(
    level=logging.NOTSET,
)

DEFAULT_FORMAT = "%(levelname)s :: %(funcName)s :: %(message)s"


def generate_logger(name: __name__, log_file: str, formatting: str = DEFAULT_FORMAT):
    """Generat a custom logger"""

    new_logger = logging.getLogger(name)
    filename = "Logging/" + log_file
    handler = logging.FileHandler(filename=filename, mode="w")
    formatter = logging.Formatter(formatting)
    handler.setFormatter(formatter)
    new_logger.addHandler(handler)
    new_logger.propagate = False

    return new_logger


new_logger_test = generate_logger(__name__ + "test_logger", "testing_logging.log")
gen_zero_logger = generate_logger(__name__ + "gen_zero_logger", "gen_zero_logging.log")


def generation_zero_logger(func: Callable[..., Any], my_logger: logging.Logger) -> Any:
    """Logging decorator for generation zero"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Starting Gen zero logging")
        val: list[object] = func()
        for instance in val:
            my_logger.info(f"Brain instance - fit - {instance.brain_id}")

        print("Ending Gen zero logging")

        return val

    return wrapper


with_generation_zero_logging = functools.partial(
    generation_zero_logger, my_logger=gen_zero_logger
)


def logging_decorator(func: Callable[..., Any]) -> Any:
    """Testing generaic logging"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Starting logging wrapper")
        val = func(*args)
        new_logger_test.info(f"New value logged - {val}")
        print("Ended Logging wrapper")

        return val

    return wrapper


# Passing in a function - the decorated function
# with Any args to make it generic
# this returns the wrapper
# wrapper takes the args, kwargs and calls the functioning given
# return of val is needed to get the vals back at the end of the wrapper
def log_count(func: Callable[..., Any]) -> Any:
    """Loggs any function"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        print("Starting in wrapper")

        # for value in func(total):
        #     print(value)

        val = func(*args)
        print(val)

        print("Ending wrapper")

        return val

    return wrapper


@logging_decorator
def count_to(total: int) -> None:
    """Filler test"""

    x: int = 0

    for i in range(total):
        x += i
        # yield x

    return x


if __name__ == "__main__":
    holder = count_to(20)
    print(holder)
