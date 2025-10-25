"""
File: Hacker.py
Description: Represents a cyberpunk hacker within the digital underworld simulation.
Theb Hacker class models a cyber-operative capable of activating rigs,
performing high-risk digital attacks, managing CryptoTokens, and handling
encrypted or unencrypted assets. It encapsulates behaviour for trace management,
rig upgrades, encryption/decryption, and secure storage interactions with the associated Rig.
This class serves as the primaty actor that coordinates actions and resources across the system.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig
from Asset import Asset
class Hacker:
    """
    Represents a hacker with a crypto token, optional linked rig, and a trace system
    that tracks digital exposure from performing high-risk actions.

    Attributes:
        __name (str): Alias of the hacker.
        __crypto_tokens (int): Digital currency for purchases/repairs.
        __rig (Rig | None): Linked rig instance when acquired.
        __trace_level (int): Current exposure level.
        __inventory (list[Asset]): Items the hacker currently holds.
    """

    def __init__(self, name):
        """
        Initialise a new Hacker instance with default starting values.

        :parameter name:
        str: A unique identifier or alias for the hacker.
        """
        self.__name = name
        self.__crypto_tokens = 1 # Hacker inventory stores 1 CryptoToken.
        self.__rig = None # Rig begins inactive, until activated.
        self.__trace_level = 0 # Trace level baseline value is set to 0.
        self.__inventory = [] # Store asset in inventory.

# ---------- Acessors ----------
    def get_trace_level(self):
        """
        Return the current trace level of the hacker.

        :returns
        int: The current numeric value of the hacker's trace level.
        """
        return self.__trace_level
    def get_name(self):
        """
        Return the hacker's name.

        :returns
        str: The hacker's alias or identifier.
        """
        return self.__name # Access and return hacker's name.
    def get_crypto_tokens(self):
        """
        Return the number of CryptoTokens currently owned.

        :returns
        int: The total number of CryptoTokens in hacker's inventory.
        """
        return self.__crypto_tokens # Access and return current amount of CryptoTokens possessed by the hacker.

    def get_rig(self):
        """
        Return the rig's activation state.

        :returns:
        Rig | None
        """
        return self.__rig # Access and return whether the hacker's rig is activated (True/False).

    # ---------- Mutators ----------

    def set_crypto_tokens(self, tokens):
        """
        Set the exact number of CryptoTokens (used by repair/awards).

        :parameter tokens:
        int: New token count.
        """
        self.__crypto_tokens = tokens

    def deduct_crypto_tokens(self, amount):
        """
        Deduct CryptoTokens safely if enough are available.

        :parameter amount:
        int: Amount to deduct (>= 0).
        """
        if self.__crypto_tokens >= amount:
            self.__crypto_tokens -= amount
        else:
            print("Insufficient CryptoTokens.")

    def set_trace_level(self, trace_level):
        """
        Set the hacker's trace level with validation.

        Behaviour:
        - Validates that the provided trace_level is an int.
        - Prevents the trace level from being set below zero.
        - Prints a notification if the trace level reaches zero (Hacker is safe/undetected).

        :parameter trace_level:
        int: The new trace level value to assign.
        :returns:
        None
        """
        if not isinstance(trace_level, int):
            raise TypeError("Trace level must be an integer value.")
        if trace_level < 0:
            raise ValueError("Trace level cannot go below the baseline value of 0.")
        self.__trace_level = trace_level
        if self.__trace_level == 0:
            print("Trace level has successfully reached 0 and you are impossible to detect.")

    # Property
    crypto_tokens = property(get_crypto_tokens, set_crypto_tokens)

    # ---------- Rig lifecycle ----------
    def acquire_rig(self, rig):
        """
        Attempt to activate the hacker's rig by spending one CryptoToken.

        Behaviour:
        - Valid rig instance required.
        - Prevents multiple acquisitions.
        - Deducts 1 token on success and links the rig.

        :parameter rig:
        Rig: The rig to link.
        """
        if isinstance(self.__rig, Rig): # Checks if there is already a rig and prevents multiple rig activations.
            print("Rig has already been activated and linked.")
        elif not isinstance(rig, Rig):
            print("Provided object is not a valid Rig. Cannot link.")
        elif self.__crypto_tokens >= 1:
            self.deduct_crypto_tokens(1)
            self.__rig = rig
            print(f"Rig has successfully linked and activated for {self.__name}")
            print(f"Rig has been paid for with 1 Crypto_Token"
                  f"\nCurrent Amount of CryptoTokens: {self.__crypto_tokens}"
                  f"\n-- Rig Activated -- State of Rig: {isinstance(self.__rig, Rig)}")
        else:
            print("-- INSUFFICIENT FUNDS TO ACTIVATE RIG -- ")

    def is_rig_active(self):
        """
        Check for rig activation.

        :returns
        Rig | None: Linked rig or None.
        """
        return self.__rig

    def repair_linked_rig(self):
        """
        Repair the linked rig (if activated), consuming 1 CryptoToken when broken.
        """
        if not self.__rig:
            print("No rig linked to repair.")
        else:
            self.__rig.repair_rig(self)

    # ---------- Risky actions (trace level)  ----------

    def byte_bomb(self):
        self.__trace_level += 3
        if self.__trace_level >= 7:
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        else:
            print("*** BYTE BOMB INITIATED ***")
            if self.__trace_level == 7:
                self.__crypto_tokens += 1
                print(f"<<< Transferring CryptoTokens into inventory: {self.__crypto_tokens} >>>")

    def neural_hack(self):
        self.__trace_level += 2
        if self.__trace_level >= 7:
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        else:
            print("*** NEURAL HACK CONNECTED ***")
            if self.__trace_level == 7:
                self.__crypto_tokens += 1
                print(f"<<< Transferring CryptoTokens into inventory: {self.__crypto_tokens} >>>")

    def server_attack(self):
        self.__trace_level += 1
        if self.__trace_level >= 7:
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        else:
            print("*** SERVER ATTACK SUCCESSFULL ***")
            if self.__trace_level == 7:
                self.__crypto_tokens += 1
                print(f"<<< Transferring CryptoTokens into inventory: {self.__crypto_tokens} >>>")

    # ---------- Concealment  ----------

    def ghost_protocol(self):
        """
        Reduce trace by 3 using validated setter (non-negative).
        """
        self.set_trace_level(self.__trace_level - 3)
    def memory_wipe(self):
        """
        Reduce trace by 2 using validated setter (non-negative).
        """
        self.set_trace_level(self.__trace_level - 2)
    def corrupt_logs(self):
        """
        Reduce trace by 1 using validated setter (non-negative).
        """
        self.set_trace_level(self.__trace_level - 1)

    # ---------- Combat  ----------
    def launch_data_attack(self, target_rig):
        """
        Launch a stored/attached Data Spike at a target rig.

        :parameter target_rig:
        Rig: The rig to attack.

        :returns:
        str: Status string for the caller to display/log.

        Behaviour:
        - Uses rig.launch_data_spikes() to consume one spike.
        - On success, applies 1 damage to target_rig.
        """
        if not self.__rig:
            print ("--- CANNOT LAUNCH ATTACK: NO ACTIVE RIG ---")
            return "--- ATTACK FAILED: NO ACTIVE RIG ---"
        if not isinstance(target_rig, Rig):
            print("--- CANNOT LAUNCH ATTACK: TARGET IS NOT A RIG ---")
            return "--- ATTACK FAILED: INVALID TARGET ---"
        print(f"{self.__name} IS LAUNCHING A DATA SPIKE AT {target_rig.get_name()}")
        spike_launched = self.__rig.launch_data_spikes()
        if spike_launched:
            target_rig.take_damage()
            return "--- ATTACK INITATED SUCCESSFULLY ---"
        return "--- ATTACK FAILED: NO SPIKES ---"

    # ---------- Inventory  ----------
    def upgrade_rig(self):
        """
        Try upgrading the linked rig using a 'Hardware Patch' in inventory.
        """
        if not self.__rig:
            print("No rig linked to upgrade.")
        else:
            self.__rig.upgrade_rig(self)

    def add_asset(self, asset):
        """
        Add an Asset instance to hacker inventory.

        :parameter asset:
        Asset: Instance to append (only valid type accepted).
        """
        if isinstance(asset, Asset):
            self.__inventory.append(asset)
            print(f"{asset.get_name()} added to inventory.")
        else:
            print("Only Asset instances can be added to inventory.")

    def remove_asset_by_name(self, asset_name):
        """
        Remove the first asset matching name from inventory and return it.

        :parameter asset_name:
        str: Case-sensitive name match.

        :returns:
        Asset | None: Removed asset, or None if not found.
        """
        available_asset = None
        new_inventory = []
        for asset in self.__inventory:
            if available_asset is None and asset.get_name() == asset_name:
                available_asset = asset
            else:
                new_inventory.append(asset)
        self.__inventory = new_inventory
        return available_asset

    def find_asset(self, asset_name):
        """
        Locate an asset by name in inventory.
        :parameters asset_name:
        asset_name: Asset name to search for in inventory.
        :returns:
        The Asset if found, otherwise None.
        """
        selected_asset = None
        for asset in self.__inventory:
            if selected_asset is None and asset.get_name() == asset_name:
                selected_asset = asset
        return selected_asset


    def encrypt_asset(self, asset_name):
        """
        Encrypt a named asset in the hacker inventory using a Security Chip.

        :parameters asset_name:
        str: Name of the asset to encrypt

        Behaviour:
        - Consumes one "Security Chip" from inventory.
        - If the asset is found, encrypts it; otherwise returns chip back.
        """
        security_chip = self.remove_asset_by_name("Security Chip")
        if security_chip is None:
            print(f"No asset named {asset_name} found in inventory.")
        else:
            assets = self.find_asset(asset_name)
            if assets is None:
                print(f"No Asset named: {asset_name} found in inventory.")
                self.add_asset(security_chip) # Return chip.
            else:
                assets.encrypt()
                print(f"{asset_name} encrypted successfully.")


    def decrypt_asset(self, asset_name):
        """
        Decrypt a named asset in the hacker inventory using a Security Chip.

        :parameter asset_name:
        str: Name of the asset to decrypt
        """
        assets = self.find_asset(asset_name)
        if assets is None:
            print(f"No asset named: {asset_name} found in inventory.")
        else:
            if not assets.is_encrypted():
                print (f"{asset_name} is already decrypted.")
            else:
                security_chip = self.remove_asset_by_name("Security Chip")
                if security_chip is None:
                    print("No Security Chip available to decrypt.")
                else:
                    assets.decrypt()
                    print(f"{asset_name} decrypted successfully.")

    def store_asset_in_rig(self, asset_name):
        """
        Move an asset from hacker inventory to linked rig storage.

        :param asset_name:
        str: Name of the asset to move.
        """
        if not self.__rig:
            print("No rig linked. Cannot store asset.")
        else:
            asset = self.remove_asset_by_name(asset_name)
            if asset:
                self.__rig.store_asset(asset)
            else:
                print(f"No asset named {asset_name} found in inventory.")

    def retrieve_asset_from_rig(self, asset_name):
        """
        Retrieve an asset from rig storage back to hacker inventory.
        :parameter asset_name:

        str: Name of the asset to retrieve.
        """
        if not self.__rig:
            print("No rig linked. Cannot retrieve asset.")
        else:
            retrieved_asset = self.__rig.release_asset(asset_name)
            if retrieved_asset:
                self.add_asset(retrieved_asset)
            else:
                print(f"No asset named {asset_name} found in rig storage.")

    def hardware_patch(self):
        """
        Create a Hardware Patch (Hacker domain) abd place it in inventory.
        """
        hardware_patch = Asset("Hardware Patch", "Used to upgrade rigs")
        self.add_asset(hardware_patch)
        print(f"{self.__name} obtained a Hardware Patch")

    def __str__(self):
        """
        Return a formatted string representation of the hacker.

        Behaviour:
        - Displays the hacker's name, linked rig name ('No Rig' if none),
        current trace level, and inventory contents.

        :returns:
        str: Readable summary of the hacker's current state.
        """
        rig_name = self.__rig.get_name() if self.__rig else "No Rig"
        inventory_list = ", ".join(str(asset) for asset in self.__inventory) if self.__inventory else "Empty"
        return (
            f"Hacker: {self.__name}\n"
            f"Rig: {rig_name}\n"
            f"Trace Level: {self.__trace_level}\n"
            f"Inventory: {inventory_list}"
        )




