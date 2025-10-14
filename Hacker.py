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
        self.__trace_level = 0


    def get_trace_level(self):
        return self.__trace_level
    def get_name(self):
        return self.__name
    def get_crypto_tokens(self):
        return self.__crypto_tokens
    def get_rig(self):
        return self.__rig

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
        self.__trace_level += 3
    def neural_hack(self):
        self.__trace_level += 2
    def data_spike(self):
        self.__trace_level += 1

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


