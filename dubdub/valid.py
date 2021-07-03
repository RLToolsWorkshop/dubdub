from pathlib import Path


def validate_file_input(input_file: Path):
    """
    Validates that the input is a file .

    Args:
        input_file (Path): The input path
    """
    assert input_file.exists(), "The path doesn't exist"
    assert input_file.is_file(), "The path isn't a file"
