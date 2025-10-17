"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig

# 1. Instantiate the Hacker and Rig objects.
print("*---- HACKER AND RIG INITIALISATION ----*")
hacker = Hacker("AnonShortforAnonymous")
rig = Rig("pc_pc(politcallycorrect_pc)")
print(hacker.get_name())
print(rig.get_name())
print(20*"___")

# 2. Display Initial Hacker state before rig activation.
print("*---- INITIAL STATUS ----*")
print("Hacker Name: ", hacker.get_name())
print("CryptoTokens: ", hacker.get_crypto_tokens())
print("Rig Activated: ", hacker.get_rig())
print("Trace Level: ", hacker.get_trace_level())


