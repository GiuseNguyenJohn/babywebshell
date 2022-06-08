#!/usr/bin/env python3
"""
A terminal application that utilizes webwizard to automate easy web CTF challenges.

Author: John Nguyen (@Magicks52)
Tested: Python 3.10.4 on Kali Linux
"""

import argcomplete
import argparse
import cmd
import subprocess
from colorama import Fore, Style
from webwizard import webwizard


def complete_cmd(text: str, options: list) -> list:
    """Takes in user-typed text and returns valid options."""

    if not text:
        completions = options
    else:
        completions = [x for x in options if x.startswith(text)]
    return completions


def cyan(text: str) -> str:
    """Return text wrapped with a cyan ANSI escape sequence."""

    return Fore.CYAN + Style.BRIGHT + text + Style.RESET_ALL


def red(text: str) -> str:
    """Return text wrapped with a red ANSI escape sequence."""

    return Fore.RED + Style.BRIGHT + text + Style.RESET_ALL


def green(text: str) -> str:
    """Return text wrapped with a green ANSI escape sequence."""

    return Fore.GREEN + Style.BRIGHT + text + Style.RESET_ALL


class BebshellInterpreter(cmd.Cmd):
    """A class that defines the behaviors of the bebshell command interpreter."""

    intro = """Welcome to bebsh.  Type help or ? to list commands.
    Type "help <cmd>" or "? cmd" to view help for a command."""
    prompt = green("(bebsh) ")

    def do_shell(self, line):
        "Run a shell command (you can also use ! <cmd>)"
        print("running shell command:", line, '\n')
        sub_cmd = subprocess.Popen(line,
                                   shell=True,
                                   stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0].decode('utf-8')
        print(output)

    def do_q(self, line):
        """Quit the program."""
        return True

    def do_EOF(self, line):
        """Quit the program."""
        return True


def main() -> None:
    # argparse
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-u", "--url", type=str, help="target url", required=True)
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    # webwizard setup
    wizard = webwizard.Wizard(args.url)
    BebshellInterpreter().cmdloop()


if __name__ == "__main__":
    main()
