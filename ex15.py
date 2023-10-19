#  sys-admin.py
import os
import subprocess

# subprocess.run(["ls","-l"])
# os.system("ls")

# You will now call subprocess.run() with three arguments. The third argument will be a directory name.
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# To emphasize that subprocess.run() allows you to run any command, you will run the df command to get disk information.
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# To emphasize that subprocess.run() allows you to run any command, you will run the df command to get disk information.
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])