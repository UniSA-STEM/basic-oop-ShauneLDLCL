"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


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
    def get_data_spikes(self):
        return self.__data_spikes

    def get_storage(self):
        return list(self.__storage)

    def is_broken(self):
        return self.__broken_state

    def get_upgrade_level(self):
        return self.__upgrade_level

    def take_damage(self):
        if self.__broken_state:
            print(f"Rig {self.__name} is already broken.")
        else:
            self.__damage_counter += 1
            print(f"Rig {self.__name} took damage! Current Damage: {self.__damage_counter}")


    def store_data_spikes(self):
        if self.__data_spikes > 0:
            for i in range(self.__data_spikes):
                self.__storage.append("Data Spike")
            print(f"{self.__data_spikes} data spikes are stored in rig storage.")
            self.__data_spikes = 0
        else:
            print("No data spikes available to store.")

    def check_storage(self):
        return "Data Spike" in self.__storage

    def launch_data_spikes(self):
        if "Data Spike" in self.__storage:
            self.__storage.remove("Data Spike")
            print("--- DATA SPIKE LAUNCHED FROM STORAGE ---")
            print(f"--- REMAINING SPIKES IN STORAGE: {self.__storage.count('Data Spike')} ---")
        elif self.__data_spikes > 0:
            self.__data_spikes -= 1
            print("*** DATA SPIKE LAUNCHED FROM RIG ***")
            print(f"--- REMAINING SPIKES ATTACHED TO RIG: {self.__data_spikes}")
        else:
            print("~~~ NO DATA SPIKES AVAILABLE!!! ~~~")






    # def launch_data_spikes(self):


    # def repair_rig(self):
    #     hacker.get_crypto_tokens()
    #     print("Current CryptoTokens: ",hacker.get_crypto_tokens())



rig = Rig("pc_pc(politicallycorrect_pc)")
print(rig.get_name())
rig.take_damage()
# rig.store_data_spikes()
# print(rig.check_storage())
# print("---")
# rig.launch_data_spikes()
# print(rig.check_storage())
# rig.launch_data_spikes()
# print(rig.check_storage())
# rig.launch_data_spikes()
# print(rig.check_storage())

# # rig.repair_rig()


