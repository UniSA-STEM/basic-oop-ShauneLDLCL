"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker, hacker


class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__data_spikes = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

    def get_name(self):
        return self.__name

    def storage(self):
        self.__storage.append(self.__data_spikes)
        print(self.__storage)

    def repair_rig(self):
        hacker.get_crypto_tokens()
        print("Current CryptoTokens: ",hacker.get_crypto_tokens())



rig = Rig("pc_pc(politicallycorrect_pc)")
print(rig.get_name())
rig.storage()
rig.repair_rig()


