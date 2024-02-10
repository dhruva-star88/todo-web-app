FILEPATH = "todos.txt"  # Its a variable, It must be in Caps and after defining it we can use that in functions


def get_todos(filepath=FILEPATH):
    """Reads the list in the text file and return the list"""  # Docstring
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):  # Always non-default parameter are followed by default parameters
    """Writes the item to the list present in the text file"""  # Docstring
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
