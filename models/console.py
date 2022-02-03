#!/usr/bin/python3
"""
This module contains the code for the custom
command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class is the foundation for the interpreter.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        This method exits the interpreter if the user
        types the command "quit".
        """
        quit()

    def do_EOF(self, arg):
        """
        This method exits the interpreter if the user
        types the EOF command (CTRL+D).
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
