import os
import sys
from datetime import datetime
# Folder Path
path = "commands"

# Change the directory
os.chdir(path)

def run_command(commands,testcase):
    file_path = os.path.join(os.path.expanduser('~'), "apps")
    save_path = os.path.join(os.path.expanduser('~'),"auto_chip_testing","BackendLogs")
    os.chdir(file_path)
    for i in range(len(commands)):
        for j in range(len(commands[i])):
            os.system(commands[i][j])
            date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
            f = open(f"{save_path}/filename_{date}", 'w')
            sys.stdout = f
            f.close()
        # date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        # f = open(f"{save_path}/filename_{date}", 'w')
        # sys.stdout = f
        # f.close()

# Read text File
def read_text_file(file_path):
    testsite_array=[]
    testcase=[]
    filterCommand = []
    with open(file_path, 'r') as f:
        for line in f:
            testsite_array.append(line)
        filter_command = filter_commands(testsite_array)
        for command in filter_command:
            if "#" not in command:
                command.replace("#","")
                testcase.append(command)
            else:
                filterCommand.append(command)

        run_command(filterCommand,testcase)


def filter_commands(commands):
    newcommand = []
    for command in commands:
        if "\n" in command:
            command = command.replace("\n","")
        if "$" not in command:
            newcommand.append(command)
    size = len(newcommand)
    idx_list = [idx + 1 for idx, val in
                enumerate(newcommand) if val == "end"]
    res = [newcommand[i: j] for i, j in
           zip([0] + idx_list, idx_list +
               ([size] if idx_list[-1] != size else []))]
    newRes = []
    for i in res:
        i.pop()
        newRes.append(i)
    return newRes

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = os.path.join(os.path.expanduser('~'),"auto_chip_testing","commands", file)
        # call read text file function
        read_text_file(file_path)
