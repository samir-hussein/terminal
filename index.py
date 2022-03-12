import platform
import socket
import time
import os
from pathlib import Path
import shutil

if not platform.system().lower() == 'windows':
    exit()


path = 'C:\\'
os.chdir(path)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
user = os.getlogin()

os.system("title Terminal V.1")
print("Terminal V.1 For Windows")

commands = {
    "help": "Get all commands",
    "ip": "Get your local ip address",
    "clear": "Clear terminal",
    "date": "Return Date",
    "time": "Return Time",
    'cd': "Change your path",
    'mkdir': "Create New Directory",
    'ls': "Show all files and directories",
    'file': "Create New File",
    'rmfile': "Remove file",
    'rmdir': "Remove directory",
    'rmdir -f': "Remove directory and all its content",
    'start': "open program",
    'open': "open file",
    'copy': "copy file",
    'cpdir': "copy directory",
    'tasklist': "Show all processes"
}


def check_command(command):
    command = command.split(' ')[0]
    if not command in commands.keys():
        return print("'" + command + "'", "is not recognized as an internal or external command")

    return True


def ip_address():
    if not command == 'ip':
        return print("'" + command + "'", "is not recognized as an internal or external command")

    print("Host Name :", host_name)
    return print("IP Address : ", host_ip)


def help():
    if not command == 'help':
        return print("'" + command + "'", "is not recognized as an internal or external command")

    for c in commands:
        print(c, ' => ', commands[c])

    return


def clear():
    if not command == 'clear':
        return print("'" + command + "'", "is not recognized as an internal or external command")

    return os.system('cls')


def date():
    if not command == 'date':
        return print("'" + command + "'", "is not recognized as an internal or external command")

    return print("Date :", time.strftime("%a, %d %b %Y"))


def get_time():
    if not command == 'time':
        return print("'" + command + "'", "is not recognized as an internal or external command")

    return print("Time :", time.strftime("%I:%M:%S %p"))


def change_dir():
    global path

    try:
        dir = command.split(' ')[1]
    except:
        # print the current directory
        return print("Current working directory is:", path)

    try:
        os.chdir(dir)
        path = os.getcwd()
        return
    except:
        return print("The system cannot find the file specified:", "'" + dir + "'")


def make_dir():
    global path
    directorys = command.replace("mkdir ", '', 1)

    if not directorys == '':
        directorys = directorys.split(" ")
    else:
        return print("Command is completed")

    for dir in directorys:
        # Path
        path_dir = os.path.join(path, dir)

        # Create the directory
        try:
            os.mkdir(path_dir)
        except:
            return print("Cannot create a directory when that directory already exists")
    return


def list():
    if not command == 'ls':
        return print("'" + command + "'", "is not recognized as an internal or external command")

    global path
    list = os.listdir(path)
    for l in list:
        print(l)
    return


def file():
    global path
    file_name = command.replace('file ', '', 1)
    if not file_name == '':
        file_name = file_name.split(" ")
    else:
        return print("Command is not completed")

    for f in file_name:
        file = path + "\\" + f

        try:
            Path(file).touch()
        except:
            return print('Failed creating the file')
    return


def rm_file():
    global path
    file_name = command.replace('rmfile ', '', 1)
    if not file_name == '':
        file_name = file_name.split(" ")
    else:
        return print("Command is not completed")

    for f in file_name:
        file = path + "\\" + f

        try:
            os.remove(file)
        except:
            return print("File not found in the directory")
    return


def rm_dir():
    global path
    if '-f' in command:
        dir_name = command.replace('rmdir -f ', '', 1)
    else:
        dir_name = command.replace('rmdir ', '', 1)

    if not dir_name == '':
        dir_name = dir_name.split(" ")
    else:
        return print("Command is not completed")

    for d in dir_name:
        dir = path + "\\" + d

        if os.path.exists(dir):

            if command.split(" ")[1] == '-f':
                shutil.rmtree(dir)
            else:
                # checking whether the folder is empty or not
                if len(os.listdir(dir)) == 0:
                    os.rmdir(dir)
                else:
                    # messaging saying folder not empty
                    return print("Folder is not empty, use rmdir -f to remove it")
        else:
            return print("The directory is not found")
    return


# open program
def start():
    program = command.replace('start ', '', 1)

    if not program == '':
        try:
            return os.system(program)
        except:
            return print("'" + program + "' not found")
    else:
        return print("Command is not completed")


# open file or directory
def open():
    file = command.replace('open ', '', 1)
    if not file == '':
        file = file.replace("'", '')
        file = file.replace('"', '')
        try:
            return os.startfile(file)
        except:
            return print("'" + file + "' not found")
    else:
        return print("Command is not completed")


def copy():
    global path
    file = command.replace("copy ", "", 1)

    if not file == '':
        file = file.split(" ")
        src = path + "\\" + file[0]
        des = path + "\\" + file[1]

        try:
            return shutil.copy(src, des)
        except:
            return print("Cannot copy this")
    else:
        return print("Command is not completed")


def copy_dir():
    global path
    dir = command.replace("cpdir ", "", 1)

    if not dir == '':
        dir = dir.split(" ")
        src = path + "\\" + dir[0]
        des = path + "\\" + dir[1]

        try:
            return shutil.copytree(src, des)
        except:
            return print("Cannot copy this")
    else:
        return print("Command is not completed")


def task_list():
    if not command == 'tasklist':
        return print("'" + command + "'", "is not recognized as an internal or external command")

    return os.system('tasklist')


command_call = {
    'help': help,
    'ip': ip_address,
    'clear': clear,
    'date': date,
    'time': get_time,
    'cd': change_dir,
    'mkdir': make_dir,
    'ls': list,
    'file': file,
    'rmfile': rm_file,
    'rmdir': rm_dir,
    'start': start,
    'open': open,
    'copy': copy,
    'cpdir': copy_dir,
    'tasklist': task_list
}


while True:
    print("")
    command = input(user + " ~ " + path + ">>> ").strip()

    if check_command(command):
        command_call[command.split(' ')[0]]()
