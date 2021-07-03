# %%
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from toolz import curry

if not TYPE_CHECKING:
	class GeneralConfig:
		arbitrary_types_allowed=True
		
	from pydantic.dataclasses import dataclass
	dataclass = curry(dataclass, config=GeneralConfig)
	

