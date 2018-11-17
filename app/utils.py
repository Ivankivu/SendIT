import string
from flask import Flask


def auto_id(_list):
    global id
    if len(_list) == 0:
        id = len(_list) + 1
    else:
        id = id + 1
    return id


def is_empty(item_list):
    if len(item_list) == 0:
        return True
    return False
