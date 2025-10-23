"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import Asset

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

    def set_broken_state(self, broken):
        self.__broken_state = broken

    def set_damage_counter(self, counter):
        self.__damage_counter = counter

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_condition(self):
        """
        Return the rig's current condition.

        :returns:
        str: A formatted string such as "Immaculate (Level 2)" or "Splintered (Level 0)".

        Behaviour:
        - Evaluates the broken state and upgrade level.
        """
        rig_condition = "Splintered" if self.__broken_state else "Immaculate"
        return f"{rig_condition} (Level {self.__upgrade_level})"

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
            return True
        elif self.__data_spikes > 0:
            self.__data_spikes -= 1
            print("*** DATA SPIKE LAUNCHED FROM RIG ***")
            print(f"--- REMAINING SPIKES ATTACHED TO RIG: {self.__data_spikes}")
            return True
        else:
            print("~~~ NO DATA SPIKES AVAILABLE!!! ~~~")
            return False

    def repair_rig(self, hacker):
        if not self.__broken_state:
            print(f"Rig {self.__name} does not require repairs.")
        elif hacker.get_crypto_tokens() >= 1:
            hacker.set_crypto_tokens(hacker.get_crypto_tokens() - 1)
            self.__damage_counter = 0
            self.__broken_state = False
            print(f"Rig {self.__name} has been repaired with 1 CryptoToken.")
        else:
            print("Insufficient CryptoTokens to repair rig.")

    def upgrade_rig(self, hacker):
        """
        Upgrade the rig using a Hardware Patch from the hacker's inventory.
        :parameter hacker:
        hacker (Hacker): The hacker who owns the rig.
        """
        hardware_patch = hacker.remove_asset_by_name("Hardware Patch")
        if hardware_patch is not None:
            self.__upgrade_level += 1
            print(f"Rig {self.__name} upgraded to Level {self.__upgrade_level}.")
        else:
            print("No Hardware Patch available for upgrade.")

    def generate_assets(self):
        """
        Randomly generate and store a new asset.

        Behaviour:
        - Adds Data Spike, Security Chip and Removable Drive

        """
        new_asset = random.choice([
            Asset("Data Spike", "Used in battles."),
            Asset("Security Chip", "Used to encrypt/decrypt assets."),
            Asset("Removable Drive", "Used for extraction.")
        ])
        self.__storage.append(new_asset)
        print(f"{self.__name} generated: {new_asset.get_name()}")


    def extract_assets(self, hacker):
        """
        Extract all unencrypted assets if rig is broken.

        :parameters hacker:
        hacker (Hacker): The hacker performing the extraction.

        Behaviour:
        - Requires one Removable Drive in hacker inventory.
        - Transfers unencrypted assets to hacker's inventory.
        """
        if not self.__broken_state:
            print(f"Rig {self.__name} is not broken. Extraction unavailable.")
        else:
            removable_drive = hacker.remove_asset_by_name("Removable Drive")
            if removable_drive is None:
                print("No Removable Drive available for extraction.")
            else:
                transferred_assets = 0
                remaining_assets = []
                for asset in self.__storage:
                    if isinstance(asset, Asset) and not asset.is_encrypted():
                        hacker.add_asset(asset)
                        transferred_assets += 1
                    else:
                        remaining_assets.append(asset)
                self.__storage = remaining_assets
                print(f"{transferred_assets} asset(s) extracted from {self.__name}.")

    def store_asset(self, asset):
        """
        Store an asset in the rig's storage.
        Behaviour:
        - Only allows Asset instances to be stored.
        - Encrypted assets cannot be stored.
        - Adds the asset to private storage if valid.
        :parameter asset:
        asset: The asset object to store.
        :returns:
        None
        """
        if not isinstance(asset, Asset):
            print("Only Asset instances can be stored in rig storage.")
        elif asset.is_encrypted():
            print(f"{asset.get_name()} is encrypted and cannot be stored.")
        else:
            self.__storage.append(asset)
            print(f"{asset.get_name()} has been stored in {self.__name}.")

    def release_asset(self, asset_name):
        """
        Remove and return an asset by name from the rig's storage.

        Behaviour:
        - Searches rig storage for the first asset with the specified name.
        - Returns the asset and removes it from rig storage.
        - Returns None if not found.
        :parameter asset_name:
        str: The name of the asset to retrieve.
        :returns:
        Asset | None: The removed asset, or None if not found.
        """
        released_asset = None
        updated_storage = []
        for asset in self.__storage:
            if released_asset is None and isinstance(asset, Asset) and asset.get_name() == asset_name:
                released_asset = asset
            else:
                updated_storage.append(asset)
        self.__storage = updated_storage
        if released_asset:
            print(f"{released_asset.get_name()} has been released from {self.__name}.")
        else:
            print(f"No asset named {asset_name} found in {self.__name}.")
        return released_asset

    def __str__(self):
        """
        Return a formatted string representation of the rig.
        Behaviour:
        - Displays the rig's name, condition (Immaculate/Splintered), upgrade level, and stored assets.
        :returns
        str: Readable summary of the rig's current condition and storage
        """
        condition_status = self.get_condition()
        store_assets_list = ", ".join(str(asset) for asset in self.__storage)
        return (
            f"Rig: {self.__name}\n"
            f"Condition: {condition_status}\n"
            f"Upgrade Level: {self.__upgrade_level}\n"
            f"Stored Assets: {store_assets_list}"
        )

