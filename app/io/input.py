import pandas as pd

def read_console(prompt: str = "Enter: ") -> str:
    """
    Read the user input from the console

    Args:
        prompt (str): The prompt to display to the user. Defaults to "Enter: "

    Returns:
        str: The user input
    """
    return input()


def read_file(file_path: str) -> str:
    """
    Read the content of a file

    Args:
        file_path (str): The path to the file

    Returns:
        str: The content of the file

    Raises:
        FileNotFoundError: If the file does not exist
    """
    with open(file_path, "r") as file:
        return file.read()


def read_file_pandas(file_path: str) -> pd.DataFrame:
    """
    Read the content of a file using pandas

    Args:
        file_path (str): The path to the file

    Returns:
        pd.DataFrame: The content of the file

    Raises:
        FileNotFoundError: If the file does not exist
        pd.errors.EmptyDataError: If the file is empty
    """
    return pd.read_csv(file_path)
