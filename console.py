import cmd
import sys

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


list_class = {"BaseModel": BaseModel, "User": User, "City": City, "Place":
              Place, "State": State, "Review": Review, "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """ Class that contains the entry point of the command interpreter"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(1)

    def do_EOF(self, arg):
        """ Exit the program quit"""
        sys.exit(1)

    def emptyline(self):
        """ Empty line"""
        pass

    def do_create(self, name_class):
        """Create a new instance of Basemodel, save it (to JSON file)
           and prints the id."""
        if not name_class:
            print("**class name missing**")
            return
        elif name_class not in list_class:
            print("** class doesn't exist **")
            return
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id.
        """
        list_arg = args.split(" ")

        if len(args) == 0:
            print("** class name missing ** ")
            return

        elif not list_arg[0] in list_class:
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            else:
                print(dict_all_obj[string])

    def do_destroy(self, class_Id):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""

        list_arg = class_Id.split(" ")

        if not class_Id:
            print("**class name missing**")
            return

        elif not list_arg[0] in list_class:
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            else:
                del(dict_all_obj[string])
                storage.save()
