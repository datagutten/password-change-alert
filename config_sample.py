# Maximum password age
max_password_age = 120
# Days before the password expires to start showing warning
warning_days = 14
# Force a password change if this file exists
# %s is replaced by the user name
# Set to None if this feature is not used
trigger_file_path = '\\\\yourserver\\chpwd$\\%s.txt'
# Ignore password change if this file exists
# Set to None if this feature is not used
ignore_file_path = '\\\\yourserver\\chpwd$\\%s_ignore.txt'
