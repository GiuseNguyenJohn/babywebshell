#!/usr/bin/env python3
"""
A terminal application that utilizes webwizard to automate easy web CTF challenges.

Author: John Nguyen (@Magicks52)
Tested: Python 3.10.4 on Kali Linux
"""

import cmd
import colorama
from webwizard import webwizard


def cyan(text: str) -> str:
    """Return text wrapped with a cyan ANSI excape sequence."""
    
    return colorama.Fore.CYAN + text + colorama.Style.RESET_ALL


class BebshellInterpreter(cmd.Cmd):
    """A class that defines the behaviors of the bebshell command interpreter."""
    
    intro = 'Welcome to babywebshell.  Type help or ? to list commands.\n'
    prompt = cyan('(bebsh) ')

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    BebshellInterpreter().cmdloop()
