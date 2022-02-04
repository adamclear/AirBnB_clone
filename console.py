#!/usr/bin/python3
"""
This module contains the code for the custom
command interpreter.
"""
import cmd
from multiprocessing.sharedctypes import Value
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
from models import storage


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

    def do_create(self, arg):
        """
        This method creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id.
        """
        if len(arg) < 1:
            print("** class name missing **")
        valid_inst = {'BaseModel': BaseModel}
        if arg in valid_inst.keys():
            new = valid_inst[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        This method prints the string representation of
        an object based on the class name and id.
        """
        if args == "":
            print("** class name missing **")
        else:
            args2 = args.split(' ')
            if len(args2) < 2:
                print("** instance id missing **")
        valid_inst = {'BaseModel': BaseModel}
        if args2[0] in valid_inst.keys():
            item_search = args2[0] + "." + args2[1]
            item_all = storage.all()
            if item_search in item_all:
                print(item_all[item_search])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        This method deletes an instance based on the
        class name and id, and saves the change into
        the JSON file.
        """
        if args == "":
            print("** class name missing **")
        else:
            args2 = args.split(' ')
            if len(args2) < 2:
                print(" instance id missing **")
        valid_inst = {'BaseModel': BaseModel}
        if args2[0] in valid_inst.keys():
            item_search = args2[0] + "." + args2[1]
            item_all = storage.all()
            if item_search in item_all:
                del item_all[item_search]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        This method prints a string representation
        of all objects based on the class name given.
        """
        if arg == "":
            print("** class name missing **")
        valid_inst = {'BaseModel': BaseModel}
        if arg in valid_inst.keys():
            print("valid class name")
            item_all = storage.all()
            print(type(item_all))
            for objs in item_all:
                print(objs)
                print(type(objs))
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
