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


all_brains_logger = generate_logger(
    __name__ + "all_brains_logger", "all_brains_logger.log"
)
fit_brains_logger = generate_logger(
    __name__ + "fit_brains_logger", "fit_brains_logger.log"
)


def generation_logging(
    func: Callable[..., Any],
    all_brain_logger: logging.Logger,
    fit_brain_logger: logging.Logger,
) -> Any:
    """Logging wrapper for Main.new_generation func"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        fit_brains, all_brains, gen_status = func(*args)
        for brain in all_brains:
            all_brain_logger.info(
                f"Brain: {brain.brain_id} - Generation: {brain.generation_num} Path: {brain.traversed_path} Fitness: {brain.fitness}"
            )
        for fit_brain in fit_brains:
            fit_brain_logger.info(
                f"Brain: {fit_brain.brain_id} - Generation: {fit_brain.generation_num} Path: {fit_brain.traversed_path} Fitness: {fit_brain.fitness}"
            )

        return fit_brains, all_brains, gen_status

    return wrapper


with_generation_logging = functools.partial(
    generation_logging,
    all_brain_logger=all_brains_logger,
    fit_brain_logger=fit_brains_logger,
)
