"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__crypto_tokens = 1
        self.__rig = False

    def get_name(self):
        return self.__name
    def get_crypto_tokens(self):
        return self.__crypto_tokens
    def get_rig(self):
        return self.__rig
