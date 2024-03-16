from app.io.input import read_console, read_file, read_file_pandas
from app.io.output import write_console


def main():
    write_console(read_console("Enter your text: "))
    write_console(read_file("./data/file.txt"))
    write_console(read_file_pandas("./data/file.csv"))


if __name__ == "__main__":
    main()
