import argparse

import subprocess

from Davinci import Davinci

parser = argparse.ArgumentParser(
                    prog='BashGPT',
                    description='What the program does')
parser.add_argument('-q', '--question', action='store_true')
parser.add_argument('-s', '--show', action='store_true')

args, unknownargs = parser.parse_known_args()
request = " ".join(unknownargs)

if args.question:
    davinci = Davinci()
    result = davinci.request(f"{request}")
    print(result)
else:
    davinci = Davinci()
    bashCommand = davinci.request(f"Write a bash command that does the following: {request}. Write only bash command.")

    if args.show:
        print(bashCommand)
    else:
        print("\n    ", end="")
        print(bashCommand)

        execute = ""
        try:
            execute = input("\nexecute? [Y/n]: ")
        except:
            execute = "N"
            print()

        if execute.strip().lower() in ["", "y"]:
            subprocess.run(bashCommand, shell=True)
