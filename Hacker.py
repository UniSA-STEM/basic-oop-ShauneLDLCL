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




