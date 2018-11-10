import string
from datetime import datetime
from flask import Flask


class Validator:

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

    def doesnot_exist(item):
        if not item or len(item) == 0:
            return jsonify({
                'message': 'Sorry! Item should at least have three characters'
            }), 400

    def is_not_integer(item):
        if type(item) == int:
            return jsonify({
                'message': 'Sorry item should be an integer'
            }), 400

    def is_negative(item):
        if item in item_list:
            if item['item_id'] != item['item_id']:
                item_list.append(item)

    def get_timestamp():
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
