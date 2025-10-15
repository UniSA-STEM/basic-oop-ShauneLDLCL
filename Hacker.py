"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

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

        Parameters
        __name (str): A unique identifier or alias for the hacker.
        """
        self.__name = name
        self.__crypto_tokens = 1 # Hacker inventory stores 1 crypto_token.
        self.__rig = False # Rig begins inactive, until activated.
        self.__trace_level = 0 # Trace level baseline value is set to 0.

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
        bool: True if the rig is active, False otherwise.
        """
        return self.__rig # Access and return whether the hacker's rig is activated (True/False).

    def acquire_rig(self):
        if self.__rig:
            print("Rig has already been activated.")
        elif self.__crypto_tokens >= 1:
            self.__crypto_tokens -= 1
            self.__rig = True
            print(f"Rig has been paid for with 1 Crypto_Token"
                  f"\nCurrent Amount of CryptoTokens: {self.__crypto_tokens}"
                  f"\n-- Rig Activated -- State of Rig: {self.__rig}")
        else:
            print("-- INSUFFICIENT FUNDS TO ACTIVATE RIG -- ")

    def byte_bomb(self):
        if self.__trace_level > 7:
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        else:
            self.__trace_level += 3
            print("*** BYTE BOMB INITIATED ***")
    def neural_hack(self):
        if self.__trace_level > 7:
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        else:
            self.__trace_level += 2
            print("*** NEURAL HACK CONNECTED ***")
    def data_spike(self):
        if self.__trace_level > 7:
            print("!!! REDUCE TRACE !!!\n-- YOU HAVE BEEN EXPOSED --")
        else:
            self.__trace_level += 1
            print("*** DATA SPIKE SUCCESSFUL ***")

# test commit is working
    def ghost_protocol(self):
        self.__trace_level -= 3
    def memory_wipe(self):
        self.__trace_level -= 2
    def corrupt_logs(self):
        self.__trace_level -= 1






# Test method

hacker = Hacker("AnonShortforAnonymous")
print(hacker.get_name())
print(hacker.get_crypto_tokens())
print(hacker.get_rig())
hacker.acquire_rig()
hacker.byte_bomb()
hacker.neural_hack()
hacker.neural_hack()
hacker.neural_hack()
hacker.byte_bomb()
hacker.byte_bomb()
hacker.byte_bomb()
hacker.ghost_protocol()
hacker.data_spike()
print(hacker.get_trace_level())




