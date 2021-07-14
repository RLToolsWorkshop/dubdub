from pathlib import Path
from subprocess import PIPE
from subprocess import run as rn
from typing import Optional

import typer
from loguru import logger
from watchgod import DefaultDirWatcher, run_process

from dubdub.repl import run_repl
from dubdub.valid import validate_file_input

state = {"is_repl": False}
app = typer.Typer(
    short_help="Run *.ddub file.",
    help="Run a file from the .ddub programming language.",
)


def run_ward():
    rn(["ward"], shell=True)


@app.command()
def ward(
    input_file: Optional[Path] = typer.Option(
        None, "-f", "--file", help="Run the file given."
    )
):
    """
    Run either the an input file or the repl if no file is supplied.
    """
    if input_file is None:
        input_file = Path.cwd()
    # logger.info(input_file)
    run_process(input_file, run_ward, watcher_cls=DefaultDirWatcher)


@app.command()
def run(
    input_file: Optional[Path] = typer.Option(
        None, "-f", "--file", help="Run the file given."
    )
):
    """
    Run either the an input file or the repl if no file is supplied.
    """
    if not input_file:
        run_repl()
        return
    validate_file_input(input_file)
    typer.echo(f"Running file {input_file.name}")
