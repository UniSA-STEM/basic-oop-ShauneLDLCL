"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    """
    Represents a digital asset (e.g., Data Spike, Security Chip, Hardware Patch).

    Attributes:
        __name (str): Human-readable item name.
        __description (str): Short explanation of the asset.
        __encrypted (bool): True if protected; encrypted assets cannot be moved/extracted.
    """
    def __init__(self, name, description):
        """
        Construct a new Asset.

        :parameter name:
        str: Display name for the asset.

        :parameter description:
        str: Short description explaining the asset's purpose.
        """
        self.__name = name
        self.__description = description
        self.__encrypted = False


    def get_name(self):
        """
        Return the asset's name.

        :returns
        str: Asset name string.
        """
        return self.__name

    def is_encrypted(self):
        """
        Indicate whether the asset is encrypted.

        :returns
        bool: True if encrypted, else False.
        """
        return self.__encrypted

    def encrypt(self):
        """
        Encrypt this asset. Repeated calls have no additional effect.
        """
        if not self.__encrypted:
            self.__encrypted = True
            print(f"{self.__name} has been encrypted.")
        else:
            print(f"{self.__name} is already encrypted.")

    def decrypt(self):
        """
        Decrypt this asset. Repeated calls have no additional effect.
        """
        if self.__encrypted:
            self.__encrypted = False
            print(f"{self.__name} has been decrypted.")
        else:
            print(f"{self.__name} is already unencrypted.")


    def __str__(self):
        """
        Return a user-friendly representation.

        :returns:
        str: "<name>: <description> [ENCRYPTED]" when encrypted, otherwise "<name>: <description>".
        """
        asset_status = " [ENCRYPTED]" if self.__encrypted else ""
        return f"{self.__name}: {self.__description}{asset_status}"