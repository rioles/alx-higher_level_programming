#!/usr/bin/python3
# 4-from_json_string.py
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.load(my_str)
