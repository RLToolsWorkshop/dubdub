from pathlib import Path
from typing import Optional

import typer

from dubdub.repl import run_repl
from dubdub.valid import validate_file_input

state = {"is_repl": False}
app = typer.Typer(
    short_help="Run *.ddub file.",
    help="Run a file from the .ddub programming language.",
)


# @app.callback()
# def callback():
#     """
#     Run the dubdub programming language.
#     """


# #     print("Hello world")
# #     if not input_file:
# #         run_repl()

# #     validate_file_input(input_file)
# #     typer.echo(f"Running file {input_file.name}")


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
