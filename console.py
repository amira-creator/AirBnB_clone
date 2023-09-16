#!/usr/bin/python3
"""The Command Line Interpreter."""

from models import *
import json
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """Class that defines Airbnb clone public class instances."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Function handle end of file character (Ctrl+D)."""

        print()
        return (True)

    def do_quit(self, line):
        """Function that exits the shell in interactive mode."""

        return (True)

    def emptyline(self):
        """Function that does nothing on ENTER."""

        pass

    def do_create(self, line):
        """Function that creates new instance of BaseModel."""

        if line == "" or line is None:
            print("** class name missing **")

        elif line not in storage.classes():
            print("** class doesn't exist **")

        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Function that prints the string representation of an instance."""

        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                patt = "{}.{}".format(words[0], words[1])
                if patt not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[patt])

    def do_destroy(self, line):
        """Function that deletes an instance based on class name and id."""

        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                patt = "{}.{}".format(words[0], words[1])
                if patt not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[patt]
                    storage.save()

    def do_all(self, line):
        """Function that prints all string representation of an instance."""

        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            else:
                new_list = [str(obj) for patt, obj in storage.all().items()
                            if type(obj).__name__ == words[0]]
                print(new_list)

        else:
            f_list = [str(obj) for patt, obj in storage.all().items()]
            print(f_list)

    def do_update(self, line):
        """Function that updates an instance based on name and id"""

        if line == "" or line is None:
            print("** class name missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, line)
        cname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")

        elif cname not in storage.classes():
            print("** class doesn't exist **")

        elif uid is None:
            print("** instance id missing **")

        else:
            patt = "{}.{}".format(cname, uid)
            if patt not in storage.all():
                print("** no instance found **")

            elif not attribute:
                print("** attribute name missing **")

            elif not value:
                print("** value missing **")

            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float

                    else:
                        cast = int

                else:
                    value = value.replace('"', '')

                attributes = storage.attributes()[cname]
                if attribute in attributes:
                    value = attributes[attribute](value)

                elif cast:
                    try:
                        value = cast(value)

                    except ValueError:
                        pass

                setattr(storage.all()[patt], attribute, value)
                storage.all()[patt].save()

    def default(self, line):
        """Function that defines default shell behaviour"""

        self.console(line)

    def console(self, line):
        """Function that defines how shell interprets commands for classes"""

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return (line)

        cname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        uid_pattern = re.search('^"([^"]*)"(?:, (.*))?$', args)

        if uid_pattern:
            uid = uid_pattern.group(1)
            attr_or_dict = uid_pattern.group(2)

        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""

        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(cname, uid, match_dict.group(1))
                return ("")

            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)

            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")

        cmd = method + " " + cname + " " + uid + " " + attr_and_value
        self.onecmd(cmd)
        return (cmd)

    def do_count(self, line):
        """Counts the instances of a class."""

        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")

        elif words[0] not in storage.classes():
            print("** class doesn't exist **")

        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def update_dict(self, cname, uid, s_dict):
        """Function to search/set dict instances in JSON file."""

        delim = s_dict.replace("'", '"')
        word = json.loads(delim)

        if not cname:
            print("** class name missing **")

        elif uid is None:
            print("** instance id missing **")

        else:
            patt = "{}.{}".format(cname, uid)
            if patt not in storage.all():
                print("** no instance found **")

            else:
                attributes = storage.attributes()[cname]
                for attribute, value in word.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)

                    setattr(storage.all()[patt], attribute, value)

                storage.all()[patt].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
