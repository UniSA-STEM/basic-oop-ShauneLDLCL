"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name, storage, removable_drive):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = storage
        self.__data_spikes = 2
        self.__removable_drive = removable_drive
        self.__upgrade_level = 0


