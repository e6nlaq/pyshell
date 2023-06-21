#!/usr/bin/env python3

# PyShell
# Copyright (C) 2023 e6nlaq

# Import
import os
import socket
import getpass
import platform

# Local Import
from lib.console.color import Color
from lib.list.csplit import csplit


def main() -> None:
    user = getpass.getuser()
    deskname = socket.gethostname()
    pwd = os.getcwd()

    print(f"PyShell 1.0.0 / {platform.system()} {platform.version()}")

    while True:
        inp = input(
            f"{Color.GREEN}{user}{Color.RESET}@{Color.MAGENTA}{deskname}{Color.RESET}: {Color.CYAN}{pwd}{Color.RESET}$ "
        )
        print(Color.RESET, end="")

        com = csplit(inp)
        func = com[0]

        if func == "exit":
            print("Logout")
            exit(0)
        elif func == "cd":
            try:
                os.chdir(com[1])
                pwd = os.getcwd()
            except FileNotFoundError:
                print(
                    f"{Color.RED}Error{Color.RESET}: The specified directory does not exist"
                )
        elif func == "ls" or func == "dir":
            files = os.listdir(pwd)
            files_file = [f for f in files if os.path.isfile(os.path.join(pwd, f))]
            files_dir = [f + "/" for f in files if os.path.isdir(os.path.join(pwd, f))]

            print(Color.GREEN + Color.BOLD + " ".join(files_dir))
            print(Color.RESET + Color.BLUE + " ".join(files_file))

        else:
            os.system(inp)

        print(Color.RESET, end="")


if __name__ == "__main__":
    main()
