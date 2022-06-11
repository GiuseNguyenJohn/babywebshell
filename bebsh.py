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
import webbrowser
from colorama import Fore, Style
from pprint import pprint
from webwizard import webwizard


def complete_cmd(text: str, options: list) -> list:
    """Takes in user-typed text and returns valid options."""
    if not text:
        return options
    else:
        return [x for x in options if x.startswith(text)]


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

    def do_robots(self, line):
        """Sends a request for robots.txt, and returns a dictionary
        with organized information if it exists."""
        pprint(self.wizard.crawl_robots())

    def do_comments(self, line):
        """Mirrors website and returns a list of js, css, and html comments."""
        print(green("[+] Mirroring {}...\n".format(self.wizard.url)))
        self.wizard.mirror()
        print(green("COMMENTS:"))
        pprint(self.wizard.get_comments())

    def do_cookies(self, line):
        """Gets any cookies sent by the server after requesting the URL."""
        pprint(self.wizard.get_cookies())

    def do_parse_for_flag(self, crib):
        """parse_for_flag <CRIB>
        Mirrors website, parses it for specified crib and returns list of possible flags."""
        if crib:
            print(green("[+] Mirroring {}...\n".format(self.wizard.url)))
            self.wizard.mirror()
            print(green("POSSIBLE FLAGS:"))
            pprint(self.wizard.parse_website_for_flag(crib))
        else:
            print(red("Crib cannot be empty!"))

    def do_shell(self, line):
        "Run a shell command (you can also use ! <cmd>)"
        print("Running shell command:", line, "\n")
        sub_cmd = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0].decode("utf-8")
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
    parser.add_argument("-u", "--url", type=str, help="target URL", required=True)
    parser.add_argument(
        "-o",
        "--open-url",
        help="open URL in a new window",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        help="directory to store mirrored files",
        required=False,
        default="/tmp/",
    )
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    # open URL if -o is specified
    if args.open_url:
        webbrowser.open(args.url, new=1, autoraise=True)
    # webwizard setup
    BebshellInterpreter.wizard = webwizard.Wizard(args.url, directory=args.directory)
    BebshellInterpreter().cmdloop()


if __name__ == "__main__":
    main()
