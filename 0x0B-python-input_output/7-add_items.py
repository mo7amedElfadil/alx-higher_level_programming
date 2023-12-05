#!/usr/bin/python3
"""Defining 7-add_items module
adds all arguments to a Python list, and then save them to a file
"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items():
    from sys import argv
    try:
        my_list = list(load_from_json_file("add_item.json"))
    except FileNotFoundError:
        save_to_json_file([], "add_item.json")
        my_list = []
    for item in argv[1:]:
        my_list.append(item)

    save_to_json_file(my_list, "add_item.json")


add_items()
