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
    """
    Represents a hacking rig (computer) that can store assets, take damage, and be upgraded.

    Attributes:
        __name (str): Rig's display name.
        __damage_counter (int): Number of hits taken.
        __broken_state (bool): True if the rig is broken.
        __storage (list[Asset]): Asset storage within the rig.
        __data_spikes (int): Loose spikes still attached to the rig (not in storage).
        __removable_drive (int): Count of built-in removable drives (baseline).
        __upgrade_level (int): Current upgrade level
    """
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__data_spikes = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

    # ----------- Accessors -----------
    def get_name(self):
        """
        Return the rig's name.

        :returns:
        str: The name assigned at initialisation.
        """
        return self.__name
    def get_data_spikes(self):
        """
        Return the number of attached data spikes that are not yet stored.

        :returns:
        int: Count of attached spikes available for launch.
        """
        return self.__data_spikes

    def get_storage(self):
        """
        Return a shallow copy of storage to preserve encapsulation.

        :returns:
        list[Asset]: Copy of current storage.
        """
        return list(self.__storage)

    def is_broken(self):
        """
        Indicate whether the rig is currently broken.

        :returns:
        bool: True if broken, otherwise False.
        """
        return self.__broken_state

    def set_broken_state(self, broken):
        """
        Mutate the broken state.

        :parameter broken:
        bool: Desired broken state.
        """
        self.__broken_state = broken

    def set_damage_counter(self, counter):
        """
        Overwrite the internal damage counter (used by repair).

        :parameter counter:
        int: New damage value.
        """
        self.__damage_counter = counter

    def get_upgrade_level(self):
        """
        Return the current upgrade level.

        :returns:
        int: Upgrade tier (0+).
        """
        return self.__upgrade_level

    # ----------- State/Condition -----------
    def get_condition(self):
        """
        Return the rig's current condition in a user-friendly phrase.

        :returns:
        str: A formatted string such as "Immaculate (Level 2)" or "Splintered (Level 0)".

        Behaviour:
        - Uses broken state and upgrade level only (simple, readable mapping).
        """
        rig_condition = "Splintered" if self.__broken_state else "Immaculate"
        return f"{rig_condition} (Level {self.__upgrade_level})"

    def take_damage(self):
        """
        Apply one unit of damage and toggle broken state if threshold reached.

        Behaviour:
        - If already broken, only report; do not increase damage.
        - Base break threshold is 2; upgrades add durability (+level).
        """
        if self.__broken_state:
            print(f"Rig {self.__name} is already broken.")
        self.__damage_counter += 1
        print(f"Rig {self.__name} took damage! Current Damage: {self.__damage_counter}")
        # Higher upgrade level increases tolerance before speaking.
        upgrade_threshold = 2 + self.__upgrade_level
        if self.__damage_counter >= upgrade_threshold:
            self.__broken_state = True
            print(f"Rig {self.__name} has become broken!")

    # ----------- Spikes & Storage -----------
    def store_data_spikes(self):
        """
        Move any attached Data Spikes into storage as Asset objects.

        Behaviour:
        - Converts attached spikes to Asset entries; resets attached count.
        """
        if self.__data_spikes > 0:
            for spikes in range(self.__data_spikes):
                spike_asset = Asset("Data Spike", "Used in battles.")
                self.__storage.append(spike_asset)
            print(f"{self.__data_spikes} data spikes are stored in rig storage.")
            self.__data_spikes = 0
        else:
            print("No data spikes available to store.")

    def check_storage(self):
        """
        Check whether at least one Data Spike is present in storage.

        :returns:
        bool: True if a stored Data Spike exists, otherwise False.
        """
        return "Data Spike" in self.__storage

    def launch_data_spikes(self):
        """
        Launch one Data Spike. Prefer stored spikes; fall back to attached spikes.

        :returns:
        bool: True if a spike was launched; False if none available.

        Behaviour:
        - Uses storage first to reward prior preparation.
        - Only Asset instances named "Data Spike" count as stored spikes.
        """
        for asset in self.__storage:
            if isinstance(asset, Asset) and asset.get_name() == "Data Spike":
                self.__storage.remove(asset)
                print("--- DATA SPIKE LAUNCHED FROM STORAGE ---")
                remaining_spikes = 0
                for spikes in self.__storage:
                    if isinstance(spikes, Asset) and spikes.get_name() == "Data Spike":
                        remaining_spikes += 1
                print(f"--- REMAINING SPIKES IN STORAGE: {self.__storage.count('Data Spike')} ---")
                return True
        if self.__data_spikes > 0:
            self.__data_spikes -= 1
            print("*** DATA SPIKE LAUNCHED FROM RIG ***")
            print(f"--- REMAINING SPIKES ATTACHED TO RIG: {self.__data_spikes}")
            return True
        print("~~~ NO DATA SPIKES AVAILABLE!!! ~~~")
        return False

    def repair_rig(self, hacker):
        """
        Repair the rig using 1 CryptoToken from the hacker, if broken.

        :parameter hacker:
        Hacker: The owner paying for the repair.

        Behaviour:
        - Resets damage and clears broken state when payment is possible.
        """
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
        Hacker: The hacker who owns the rig.
        """
        hardware_patch = hacker.remove_asset_by_name("Hardware Patch")
        if hardware_patch is not None:
            self.__upgrade_level += 1
            print(f"Rig {self.__name} upgraded to Level {self.__upgrade_level}.")
        else:
            print("No Hardware Patch available for upgrade.")

    # ----------- Asset Generation and Movement -----------
    def generate_assets(self):
        """
        Randomly generate and store a new asset.

        Behaviour:
        - Generates either a Security Chip or a Removable Drive here
          (Data Spikes are handled via store_data_spikes()).
        """
        new_asset = random.choice([
            Asset("Security Chip", "Used to encrypt/decrypt assets"),
            Asset("Removable Drive", "Used for extraction")
        ])
        self.__storage.append(new_asset)
        print(f"{self.__name} generated: {new_asset.get_name()}")

    def display_storage(self, title):
        """
        Print the storage contents line-by-line using Asset.__str__.

        :parameter title:
        str: Heading to print above the list.
        """
        print(title)
        if not self.__storage:
            print(" - Storage is empty.")
        else:
            for asset in self.__storage:
                print(f" - {asset}")


    def extract_assets(self, hacker):
        """
        Extract all unencrypted assets if rig is broken and hacker has a Removable Drive.

        :parameter hacker:
        Hacker: The hacker performing the extraction.


        Behaviour:
        - Consumes one Removable Drive from hacker.
        - Transfers all unencrypted assets from rig storage to hacker inventory.
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

        :parameter asset:
        Asset: The asset object to store.

        Behaviour:
        - Only allows Asset instances to be stored.
        - Encrypted assets cannot be stored.
        - Storage capacity increases with each upgrade level.
          (Base capacity = 3 assets + 1 per upgrade level)
        - Prints informative feedback if capacity limit is reached.
        """
        # Calculate dynamic storage limit (upgrade increases capacity)
        storage_limit = 3 + self.__upgrade_level

        # Reject if full — enforces upgrade effect on storage
        if len(self.__storage) >= storage_limit:
            print(f"Storage full. Upgrade required to store more assets "
                  f"(Limit: {storage_limit} items).")

        # Validate that only valid Asset objects are stored
        elif not isinstance(asset, Asset):
            print("Only Asset instances can be stored in rig storage.")

        # Encrypted assets cannot be placed into rig storage
        elif asset.is_encrypted():
            print(f"{asset.get_name()} is encrypted and cannot be stored.")

        # Successful storage if all checks pass
        else:
            self.__storage.append(asset)
            print(f"{asset.get_name()} successfully added to rig storage.")
            print(f"Storage usage: {len(self.__storage)}/{storage_limit}")

    def release_asset(self, asset_name):
        """
        Remove and return an asset by name from the rig's storage.

        :parameter asset_name:
        str: The name of the asset to retrieve.

        :returns:
        Asset | None: The removed asset, or None if not found.

        Behaviour:
        - Returns the first asset with a matching name.
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

        :returns:
        str: Readable summary of the rig's name, current condition upgrade level, and stored assets list.
        """
        condition_status = self.get_condition()
        store_assets_list = ", ".join(str(asset) for asset in self.__storage)
        return (
            f"Rig: {self.__name}\n"
            f"Condition: {condition_status}\n"
            f"Upgrade Level: {self.__upgrade_level}\n"
            f"Stored Assets: {store_assets_list}"
        )

