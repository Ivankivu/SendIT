import string  # pragma: no cover
import re
from numbers import Number
from datetime import datetime  # pragma: no cover
from flask import Flask, jsonify  # pragma: no cover


class Validator:  # pragma: no cover

    def validate3(item, item2, item3):

        if isinstance(item, int) or isinstance(item2, int) or isinstance(item3, int):
            return jsonify({'message': 'Invalid Input'})
        if not str.isalpha(item) or not str.isalpha(item2) or not not str.isalpha(item3):
            return jsonify({"message": "Invalid input!!"})

    def is_empty(str):
        if str == 0:
            return True
        return False

    def validate_name(name):
        if name and len(name) < 3:
            return True
        return False

    def is_email(item):
        if not r'[\w\.-]+@[\w\.-]+':
            raise Exception("please enter a valid email!!")

    def is_not_integer(int):
        if not int:
            return jsonify({
                'message': 'Sorry item should be an integer'
            }), 400

    def isspace(str):
        if str and not str.isspace():
            print('not null and not empty nor whitespace')
        else:
            print('null or empty or whitespace')

    def password(item):
        if not item:
            raise Exception("Field can't be empty")
        if len(item) < 8 or len(item) > 12:
            raise Exception(
                "Weak password. Password must be 8 characters long")
        if not re.search(r'[0-9]', item):
            raise Exception(
                'Weak password. Password should have atleast one integer')
        if item.isupper() or item.isdigit():
            raise Exception('Very Weak password')

    def get_timestamp():
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
