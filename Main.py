"""
File: main.py
Description: Simulation and testing of the Hacker, Rig, and Asset classes.
This file demonstrates the system's full functionality of the system.
It instantiates hackers, rigs, and assets, and simulates key interactions such as
rig activation, upgrades, battles, encryption/decryption, and trace management.
Edge cases are also tested, including attempts to upgrade without a rig,
encrypt without a Security Chip, and attack under high trace conditions.
as it instantiates hackers, rigs, and assets
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset

# _______________________________________________________
# 1. INITIALISATION
# _______________________________________________________
print("------------- HACKER AND RIG INITIALISATION -------------")
# Create a hacker and a rig to begin the simulation.
# This verifies that constructors (__init__) assign default attributes correctly.
hacker = Hacker("AnonymousHacker")
rig = Rig("RiggedRig")
# Display each object's readable summary using each class's __str__ representations..
print(hacker)
print(rig)
# Quick identity checks
print("Hacker Name:",hacker.get_name())
print("Rig Name:",rig.get_name())
print(20*"___")

# _______________________________________________________
# 2. INITIAL STATUS CHECK
# _______________________________________________________
print("------------- INITIAL STATUS -------------")
print("Hacker Name: ", hacker.get_name())
print("CryptoTokens: ", hacker.get_crypto_tokens()) # 1 by default
print("Rig Activated: ", hacker.get_rig()) # None before rig is activated
print("Trace Level: ", hacker.get_trace_level()) # Starts at 0
print(20*"___")

# _______________________________________________________
# 3. UPGRADE WITHOUT RIG
# _______________________________________________________
print("------------- ATTEMPT UPGRADE WITHOUT RIG -------------")
hacker.upgrade_rig() # Expected: returns "No rig linked to upgrade."
print(20*"___")

# _______________________________________________________
# 4. RIG ACTIVATION
# _______________________________________________________
print("------------- RIG ACTIVATION -------------")
hacker.acquire_rig(rig) # Costs 1 CryptoToken
print(f"Rig Activated: {'ACTIVE' if hacker.is_rig_active() else 'INACTIVE'}")
print("Remaining Tokens: ", hacker.get_crypto_tokens())
print(20*"___")

# _______________________________________________________
# 5. RIG ASSET GENERATION
# _______________________________________________________
print("------------- RIG GENERATION -------------")
rig.generate_assets()
rig.generate_assets()
# Invoke display method to print stored assets in readable form.
rig.display_storage("Rig storage (after generation):")
print(20*"___")

# _______________________________________________________
# 6. STORING AND RETRIEVING ASSETS
# _______________________________________________________
print("------------- STORE & RETRIEVE ASSET -------------")
# Give hacker a Hardware Patch in inventory & show inventory summary.
hacker.add_asset(Asset("Hardware Patch", "Used to upgrade rigs"))
print("Hacker inventory before storing:", hacker)
# Move the Hardware Patch to the linked rig's storage.
hacker.store_asset_in_rig("Hardware Patch")
rig.display_storage("Rig storage after storing:")
# Retrieve it back to the hacker.
hacker.retrieve_asset_from_rig("Hardware Patch")
print("Hacker inventory after retrieving:", hacker)
print(20*"___")

# _______________________________________________________
# 7. RISKY HACKING ACTIONS - TRACE SIMULATION
# _______________________________________________________
print("------------- RISKY HACKING ACTIONS -------------")
hacker.byte_bomb() # +3 trace
hacker.neural_hack() # +2 trace
hacker.server_attack() # +1 trace
hacker.server_attack() # +1 trace - reach reward threshold.
# hacker.neural_hack() - # Testing CryptoToken reward handling.
print("Trace Level after risky actions: ", hacker.get_trace_level())
# Try another attack to show behaviour when trace >= threshold.
hacker.server_attack()
print("Trace Level after risky actions: ", hacker.get_trace_level())
print("CryptoTokens after risky actions: ", hacker.get_crypto_tokens())
print(20*"___")

# _______________________________________________________
# 8. CONCEALMENT ACTIONS - TRACE REDUCTION
# _______________________________________________________
print("------------- CONCEALMENT ACTIONS -------------")
# Concealment actions reduces trace.
hacker.corrupt_logs() # -1 trace
hacker.memory_wipe() # -2 trace
hacker.ghost_protocol() # -3 trace
hacker.corrupt_logs() # -1 trace
# hacker.corrupt_logs() - # Testing and debugging ValueError.
print("Trace level after concealment actions: ", hacker.get_trace_level())
print(20*"___")

# _______________________________________________________
# 9. BATTLE SIMULATION
# _______________________________________________________
print("------------- BATTLE SIMULATION -------------")
# A digital “battle” between hacker and rig — simulates Data Spike attacks.
# Repeated attacks damage the rig until it breaks (testing is_broken and take_damage logic).
rig.store_data_spikes()
rig.display_storage("Rig Storage Before Battle:")
print("--- BATTLE BEGINS ---")

# Attack multiple times to simulate ongoing digital conflict.
for round_num in range(1, 5):
    print(f"\nRound {round_num}: Launching attack...")
    hacker.launch_data_attack(rig)
    # Even if the rig breaks, the simulation continues to display state evolution.
    print(f"Rig Broken State: {rig.is_broken()}")

print("--- BATTLE ENDS ---")
rig.display_storage("Rig Storage After Battle:")
print(rig)
print(20*"___")

# _______________________________________________________
# 10. ASSET EXTRACTION AFTER BATTLE
# _______________________________________________________
print("------------- ASSET EXTRACTION TEST -------------")
# When rig is broken, hacker uses a Removable Drive to extract unencrypted assets.
rig.set_broken_state(True)
hacker.add_asset(Asset("Removable Drive", "Used for extraction"))
rig.extract_assets(hacker)
print(20*"___")

# _______________________________________________________
# 11. RIG MAINTENANCE - UPGRADE AND REPAIR
# _______________________________________________________
print("------------- RIG MAINTENANCE & UPGRADE -------------")
# Tests Hardware Patch upgrades and CryptoToken-based repairs.
hacker.hardware_patch()
hacker.upgrade_rig()
hacker.repair_linked_rig()
print(20*"___")

# _______________________________________________________
# 12. ENCRYPTION AND EDGE CASES
# _______________________________________________________
print("------------- ENCRYPTION TEST -------------")
# Demonstrates encryption/decryption logic and edge handling (missing chip).
confidential = Asset("Confidential File", "Top Secret Data")
hacker.add_asset(confidential)

# Attempt encryption without a Security Chip (should fail safely).
print("Attempting to encrypt without a Security Chip:")
hacker.encrypt_asset("Confidential File")

# Add a Security Chip and try again.
hacker.add_asset(Asset("Security Chip", "Used to encrypt/decrypt assets."))
print("Attempting encryption again with chip:")
hacker.encrypt_asset("Confidential File")

# Add another chip for decryption and perform reverse operation.
hacker.add_asset(Asset("Security Chip", "Used to encrypt/decrypt assets."))
print("Attempting decryption:")
hacker.decrypt_asset("Confidential File")
print(20 * "___")

# _______________________________________________________
# 13. ENCRYPTION AND EDGE CASES
# _______________________________________________________

print("------------- STORAGE CAPACITY UPGRADE TEST -------------")
# Check that rig storage capacity increases with upgrades.

# Fill storage close to its limit (base = 3 items at Level 0).
print("Filling storage to base limit...")
for file_num in range(4):  # 4th item should exceed the limit
    rig.store_asset(Asset(f"File {file_num + 1}", "Test Data"))

print(f"Stored items before upgrade: {len(rig.get_storage())}")

# Upgrade the rig to unlock extra capacity.
print("\nUpgrading rig to expand storage capacity...")
hacker.hardware_patch()
hacker.upgrade_rig()

# Add more files after upgrade (capacity should now allow more).
for file_num in range(4, 6):
    rig.store_asset(Asset(f"File {file_num + 1}", "Post-upgrade data"))

print(f"Stored items after upgrade: {len(rig.get_storage())}")
rig.display_storage("Rig Storage After Upgrade:")
print(20 * "___")

# _______________________________________________________
# 14. ENCRYPTION AND EDGE CASES
# _______________________________________________________
print("------------- FINAL SYSTEM STATE -------------")
# Displays the end-state of both Hacker and Rig objects.
print(hacker)
print(rig)
print("------------- END OF SIMULATION -------------")
