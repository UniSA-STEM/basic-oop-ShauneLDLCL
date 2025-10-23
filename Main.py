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
from Asset import Asset

# 1. Instantiate the Hacker and Rig objects.
print("------------- HACKER AND RIG INITIALISATION -------------")
hacker = Hacker("AnonShortforAnonymous")
print(hacker)
rig = Rig("pc_pc(politcallycorrect_pc)")
print(rig)
print(hacker.get_name())
print(rig.get_name())
print(20*"___")

# 2. Display Initial Hacker state before rig activation.
print("------------- INITIAL STATUS -------------")
print("Hacker Name: ", hacker.get_name())
print("CryptoTokens: ", hacker.get_crypto_tokens())
print("Rig Activated: ", hacker.get_rig())
print("Trace Level: ", hacker.get_trace_level())
print(20*"___")

# 3. Attempt upgrade without rig.
print("------------- ATTEMPT UPGRADE WITHOUT RIG -------------")
hacker.upgrade_rig()
print(20*"___")

# 4. Activate the rig using the Hacker's CryptoTokens.
print("------------- RIG ACTIVATION -------------")
hacker.acquire_rig(rig)
print(f"Rig Activated: {'ACTIVE' if hacker.is_rig_active() else 'INACTIVE'}")
print("Remaining Tokens: ", hacker.get_crypto_tokens())
print(20*"___")

# 5. Rig generates some assets.
print("------------- RIG GENERATION -------------")
rig.generate_assets()
rig.generate_assets()
rig.display_storage("Rig storage (after generation):")
print(20*"___")

# 6. Hacker stores an item into the rig then retrieves it.
print("------------- STORE & RETRIEVE ASSET -------------")
# hacker obtains an asset and stores it
hacker.add_asset(Asset("Hardware Patch", "Used to upgrade rigs."))
print("Hacker inventory before storing:", hacker)
hacker.store_asset_in_rig("Hardware Patch")
rig.display_storage("Rig storage after storing:")
hacker.retrieve_asset_from_rig("Hardware Patch")
print("Hacker inventory after retrieving:", hacker)
print(20*"___")

# 7. Execute hacking operations that increase trace level and transfer CryptoTokens to inventory.
print("------------- RISKY HACKING ACTIONS -------------")
hacker.byte_bomb()
hacker.neural_hack()
hacker.server_attack()
hacker.server_attack()
# hacker.neural_hack() - # Testing CryptoToken reward handling.
print("Trace Level after risky actions: ", hacker.get_trace_level())
hacker.server_attack()
print("Trace Level after risky actions: ", hacker.get_trace_level())
print("CryptoTokens after risky actions: ", hacker.get_crypto_tokens())
print(20*"___")

# 5. Perform concealment operations to reduce trace level.
print("------------- CONCEALMENT ACTIONS -------------")
hacker.corrupt_logs()
hacker.memory_wipe()
hacker.ghost_protocol()
hacker.corrupt_logs()
# hacker.corrupt_logs() - # Testing and debugging ValueError.
print("Trace level after concealment actions: ", hacker.get_trace_level())
print(20*"___")

# 6. Store and launch Data Spikes from the rig.
print("------------- RIG STORAGE TEST & ATTACK TEST -------------")
rig.store_data_spikes()
rig.display_storage("Rig Storage Contents:")
hacker.launch_data_attack(rig)
print(20*"___")

# 7. Upgrade, repair, and extract assets.
print("------------- RIG MAINTENANCE & UPGRADE -------------")
hacker.hardware_patch()
hacker.upgrade_rig()
hacker.repair_linked_rig()
print(20*"___")

# 8. Generate and encrypt assets to test encryption logic.
print("------------- ENCRYPTION TEST -------------")
assets = Asset("Confidential File", "Top Secret Data")
hacker.add_asset(assets)
assets.encrypt()
assets.decrypt()
print(20*"___")
