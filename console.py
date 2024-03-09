#!/usr/bin/python3
""" Command interpreter module """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """ Create a new instance """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        new_instance = eval("{}()".format(class_name))
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Show instance information """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, arg_list[1])
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Destroy instance """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, arg_list[1])
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Show all instances """
        all_objs = storage.all()
        if not arg:
            for obj in all_objs.values():
                print(str(obj))
        else:
            arg_list = arg.split()
            class_name = arg_list[0]
            if class_name not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
                return
            new_obj = obj.__class__.__name__
            for obj in all_objs.values():
                if new_obj == class_name:
                    print(str(obj))

    def do_update(self, arg):
        """ Update instance attribute """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, arg_list[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        attr_name = arg_list[2]
        attr_value = arg_list[3]
        obj = all_objs[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """ Quit command to exit the program """
        sys.exit()

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print("")
        return True

    def emptyline(self):
        """ Do nothing on empty input line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
