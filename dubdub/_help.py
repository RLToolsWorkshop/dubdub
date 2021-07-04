from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from toolz import curry


class GenConfig:
    arbitrary_types_allowed = True


if not TYPE_CHECKING:

    from pydantic.dataclasses import dataclass
