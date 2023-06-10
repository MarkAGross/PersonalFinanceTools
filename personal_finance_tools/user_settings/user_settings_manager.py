import definitions
import os
import shutil


class UserSettingsManager:
    """Manages user settings of Personal Finance tools for the user running the application"""

    def __init__(self):
        self.user_account_name = os.getlogin()

        # Initialize settings directory and files for user if they don't exist
        _initialize_settings_dir(self.user_account_name)


def _initialize_settings_dir(username):
    """
    Sets up custom settings directory for user
    :param username: username of the user to create a custom settings directory for
    """
    settings_dir = os.path.join(definitions.USERS_CUSTOM_SETTINGS_DIR, username)

    # If user's custom settings directory does not exist, create it
    if not os.path.exists(settings_dir):
        os.makedirs(settings_dir)

    # Copy any default files from default settings not in custom settings directory
    default_settings_files = os.listdir(definitions.USERS_DEFAULT_SETTINGS_DIR)
    custom_settings_files = os.listdir(settings_dir)
    for default_file in default_settings_files:
        if default_file not in custom_settings_files:
            shutil.copy(src=default_file, dst=definitions.USERS_CUSTOM_SETTINGS_DIR)
