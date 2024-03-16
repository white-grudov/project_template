def write_console(output: str):
    """
    Write the output to the console

    Args:
        output (str): The output to write
    """
    print(output)


def write_file(file_path: str, output: str):
    """
    Write the output to a file

    Args:
        file_path (str): The path to the file
        output (str): The output to write
    """
    with open(file_path, "w") as file:
        file.write(output)
