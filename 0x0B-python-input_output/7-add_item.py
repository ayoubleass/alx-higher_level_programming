#!/usr/bin/python3
"""
    This skript  adds all arguments to a Python list,
    and then save them to a file
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """
    Check if there are additional arguments (excluding the script name)
    """
    new_list = argv[1:]
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    new_list = items + new_list
    save_to_json_file(new_list, "add_item.json")
    print(new_list)


if __name__ == "__main__":
    main()
