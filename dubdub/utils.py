# %%
from pathlib import Path
from typing import Generator, List, Union

from lark import Lark, Transformer, v_args
from lark.visitors import Interpreter, visit_children_decor
from rich import print


def rel_dir(loc: Union[Path, str], *extras: str) -> Path:
    rel_path = get_dir(Path(loc))
    return rel_path.joinpath(*extras)


def lark_rules(name: str = "rules.lark", rel_to: Union[Path, str] = __file__):
    return Lark.open(name, parser="lalr", rel_to=str(rel_dir(rel_to)))


def get_dir(loc: Path) -> Path:
    if loc.is_dir():
        return loc
    return loc.parent


def get_lang_files(
    extension: str, relation: Path = Path(__file__)
) -> Generator[Path, None, None]:

    ext = extension.lstrip(".")
    feature_path = get_dir(Path(relation))
    glob_pattern = f"**/*.{ext}"
    return feature_path.glob(glob_pattern)
