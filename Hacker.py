"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig
from Asset import Asset
class Hacker:
    """
    Represents a hacker with a crypto token, rig activation, and a trace system
    that tracks digital exposure from performing high-risk actions.

        Attributes
        __name (str): The hacker's chosen alias or display name
        __crypto_tokens (int): The amount of digital currency available to the hacker.
        __rig (bool): Indicates whethere the hacker's rig is active or inactive.
        __trace_level (int): A measure of the risk of exposure. Increases when actions are risky
        and reduces when concealment actions are executed.
    """

    def __init__(self, name):
        """
        Initialise a new Hacker instance with default starting values.

        :parameter
        __name (str): A unique identifier or alias for the hacker.
        """
        self.__name = name
        self.__crypto_tokens = 1 # Hacker inventory stores 1 CryptoToken.
        self.__rig = None # Rig begins inactive, until activated.
        self.__trace_level = 0 # Trace level baseline value is set to 0.
        self.__inventory = [] # Store asset in inventory.

# Accessor (Getter) methods
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

        :returns:
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

    # Setter (Mutator) methods

    def set_crypto_tokens(self, tokens):
        self.__crypto_tokens = tokens

    def deduct_crypto_tokens(self, amount):
        if self.__crypto_tokens >= amount:
            self.__crypto_tokens -= amount
        else:
            print("Insufficient CryptoTokens.")

    def set_trace_level(self, trace_level):
        """
        Set the hacker's trace level with validation.

        Behaviour:
        Validates that the provided trace_level is an int.
        Prevents the trace level from being set below zero.
        Prints a notification if the trace level reaches zero (Hacker is safe/undetected).

        :parameter trace_level:
        trace_level (int): The new trace level value to assign.
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

#     Property
    crypto_tokens = property(get_crypto_tokens, set_crypto_tokens())

# Acquire rig method
    def acquire_rig(self, rig):
        """
        Attempt to activate the hacker's rig by spending one CryptoToken.

        Behaviour
        If the rig is already active, prints a message and outputs nothing.
        If at least one CryptoToken is available, deducts one token, activates the rig and changes the state of
        the rig to True.
        Otherwise, the hacker is notified of insufficient funds to activate the rig.

        :parameter
        None
        :returns
        None
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
        return self.__rig

    def repair_linked_rig(self):
        if not self.__rig:
            print("No rig linked to repair.")
        else:
            self.__rig.repair_rig(self)



    def byte_bomb(self):
        if self.__trace_level >= 7:
            self.__trace_level += 3
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        elif self.__trace_level < 7:
            self.__trace_level += 3
            print("*** BYTE BOMB INITIATED ***")
            if self.__trace_level == 7:
                self.__crypto_tokens += 1
                print(f"<<< Transferring CryptoTokens into inventory: {self.__crypto_tokens} >>>")
            # elif self.__trace_level > 7:
            #     self.__trace_level += 3
            #     print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")

    def neural_hack(self):
        if self.__trace_level >= 7:
            self.__trace_level += 2
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        elif self.__trace_level < 7:
            self.__trace_level += 2
            print("*** NEURAL HACK CONNECTED ***")
            if self.__trace_level == 7:
                self.__crypto_tokens += 1
                print(f"<<< Transferring CryptoTokens into inventory: {self.__crypto_tokens} >>>")
            # elif self.__trace_level > 7:
            #     self.__trace_level += 2
            #     print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")

        # elif self.__trace_level < 7:
        #     self.__trace_level += 2
        #     print("*** NEURAL HACK CONNECTED ***")
    def server_attack(self):
        if self.__trace_level >= 7:
            self.__trace_level += 1
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        elif self.__trace_level < 7:
            self.__trace_level += 1
            print("*** SERVER ATTACK SUCCESSFULL ***")
            if self.__trace_level == 7:
                self.__crypto_tokens += 1
                print(f"<<< Transferring CryptoTokens into inventory: {self.__crypto_tokens} >>>")
            # elif self.__trace_level > 7:
            #     self.__trace_level += 1
            #     print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")

    def ghost_protocol(self):
        self.set_trace_level(self.__trace_level - 3)
    def memory_wipe(self):
        self.set_trace_level(self.__trace_level - 2)
    def corrupt_logs(self):
        self.set_trace_level(self.__trace_level - 1)

    def launch_data_attack(self, target_rig):
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

    def upgrade_rig(self):
        if not self.__rig:
            print("No rig linked to upgrade.")
        else:
            self.__rig.upgrade_rig(self)

    def add_asset(self, asset):
        """
        Add an Asset istance to hacker inventory.
        """
        if isinstance(asset, Asset):
            self.__inventory.append[asset]
            print(f"{asset.get_name()} added to inventory.")
        else:
            print("Only Asset instances can be added to inventory.")

    def remove_asset_by_name(self, asset_name):
        """
        Remove the first asset matching name from inventory and return it.
        Returns None if not found.
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

    def hardware_patch(self):
        """
        Acquire a Hardware Patch (Hacker domain) abd place it in inventory.
        """
        hardware_patch = Asset("Hardware Patch", "Used to upgrade rigs.")
        self.add_asset(hardware_patch)
        print(f"{self.__name} obtained a Hardware Patch")







# Test method

# hacker = Hacker("AnonShortforAnonymous")
# print(hacker.get_name())
# print(hacker.get_crypto_tokens())
# print(hacker.get_rig())
# hacker.acquire_rig()
# hacker.byte_bomb() # 3
# hacker.neural_hack() # 2
# hacker.neural_hack() # 2
# hacker.neural_hack() # 2
# print(hacker.get_trace_level())
# print(hacker.get_crypto_tokens())
# hacker.ghost_protocol() # - 3
# hacker.corrupt_logs() # - 1
# hacker.neural_hack() # 2
# hacker.neural_hack() # 2
# print(20*"-")
# print(hacker.get_trace_level())
# print(hacker.get_crypto_tokens())
# hacker.byte_bomb() # 3
# hacker.ghost_protocol()
# print(hacker.get_trace_level())
# print(hacker.get_trace_level())
# hacker.byte_bomb()
# hacker.byte_bomb()
# hacker.byte_bomb()
# hacker.byte_bomb()
# hacker.server_attack()
# hacker.byte_bomb()
# print(hacker.get_trace_level())
# print(hacker.data_spikes())




