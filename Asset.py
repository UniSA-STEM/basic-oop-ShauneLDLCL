"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, desccription):
        self.__name = name
        self.__description = desccription
        self.__encrypted = False


    def get_name(self):
        return self.__name

    def is_encrypted(self):
        return self.__encrypted

    def encrypt(self):
        if not self.__encrypted:
            self.__encrypted = True
            print(f"{self.__name} has been encrypted.")
        else:
            print(f"{self.__name} is already encrypted.")

    def decrypt(self):
        if self.__encrypted:
            self.__encrypted = False
            print(f"{self.__name} has been decrypted.")
        else:
            print(f"{self.__name} is already unencrypted.")


    def __str__(self):
        return f"{self.__name}: {self.__description} [ENCRYPTED]" if self.__encrypted else f"{self.__name}: {self.__description}"