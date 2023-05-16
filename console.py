#!/usr/bin/python3
"""
    console class
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        class contains entry point of the command
        interpreter
    """
    prompt = '(hbnb)'
    class_list = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']

    def do_EOF(self, args):
        """
            EOF to exit console
        """
        return True

    def do_quit(self, args):
        """
            Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
            an empty line + ENTER shouldn't
            execute
        """
        pass

    def postloop(self):
        """
            to do nothing after each loop
        """
        pass

    def do_create(self, args):
        """
            Creates new instance of BaseModel
            saves to JSON file
            and prints the id
        """
        cogs = args.split()
        if len(cogs) == 0:
            print("** class name missing **")
            return
        elif cogs[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        instance = eval(cogs[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, args):
        """
            prints string representation of
            an instance based on class name and id
        """
        cogs = args.split()
        if len(cogs) == 0:
            print("** class name missing **")
            return
        if cogs[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(cogs) == 1:
            print("** instance id is missing **")
            return
        all_objects = models.storage.all()
        for objects_id in all_objects.keys():
            if objects_id == cogs[1] and cogs[0]\
                    in str(type(all_objects[objects_id])):
                print(all_objects[objects_id])
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id
        """
        cogs = args.split()
        if len(cogs) == 0:
            print("** class name missing **")
            return
        if cogs[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(cogs) == 1:
            print("** instance id is missing **")
            return
        all_objects = models.storage.all()
        for objects_id in all_objects.keys():
            if objects_id == cogs[1] and cogs[0]\
                    in str(type(all_objects[objects_id])):
                del all_objects[objects_id]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """
            Prints all string representation
            based on or not on class name
        """
        cogs = args.split()
        all_objects = models.storage.all()
        print_all = []
        if len(cogs) == 0:
            for v in all_objects.values():
                print_all.append(str(v))
        elif cogs[0] in HBNBCommand.class_list:
            for k, v in all_objects.items():
                if cogs[0] in k:
                    print_all.append(str(v))
        else:
            print("** class doesn't exist **")
            return False
        print(print_all)

    def do_update(self, args):
        """
            Updates instance based on class name and id
        """
        cogs = args.split()
        if len(cogs) == 0:
            print("** class name missing **")
            return
        if cogs[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(cogs) == 1:
            print("** instance id missing **")
            return
        if len(cogs) == 2:
            print("** attribute name missing **")
            return
        if len(cogs) == 3:
            print("** value missing **")
            return
        all_objects = models.storage.all()
        for objects_id in all_objects.keys():
            if objects_id == cogs[1]:
                setattr(all_objects[objects_id], cogs[2], cogs[3])
                models.storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
