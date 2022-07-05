#!/usr/bin/python3
# 3-write_file.py
"""Defines a file-writing function."""
def write_file(filename="", text=""):
    """Write a string to a UTF8 text file

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write the file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

