from pathlib import Path

def read_file(path_input):
    file_path = Path(path_input)

    try:
        with file_path.open('r', encoding='utf-8') as file:
            data = file.read()
            return data

    except FileNotFoundError:
        print(f"No such file '{file_path}' exists.")
        return None

    except PermissionError:
        print(f"No permission to read the file '{file_path}'.")
        return None
