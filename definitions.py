import os

######################################
# Args Help
######################################
APP_DESCRIPTION = "This application provides tools to manage your personal finances."
DEFAULT_APP_MODE = "cli"

######################################
# Root Project
######################################
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

######################################
# Personal Finance CLI
######################################
PERSONAL_FINANCE_CLI_DIR = os.path.join(ROOT_DIR, 'command_line_interface')

######################################
# Personal Finance Tools
######################################
PERSONAL_FINANCE_TOOLS_DIR = os.path.join(ROOT_DIR, 'personal_finance_tools')
USER_SETTINGS_DIR = os.path.join(PERSONAL_FINANCE_TOOLS_DIR, 'user_settings')

######################################
# User Settings
######################################
USERS_SETTINGS_ROOT_DIR = os.path.join(ROOT_DIR, 'settings')
USERS_DEFAULT_SETTINGS_DIR = os.path.join(USERS_SETTINGS_ROOT_DIR, 'default')
USERS_CUSTOM_SETTINGS_DIR = os.path.join(USERS_SETTINGS_ROOT_DIR, 'user')
