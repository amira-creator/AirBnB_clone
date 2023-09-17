#!/usr/bin/python3
"""modlue Unittest for console of Airbnb clone"""

from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import tests
import unittest
import console
import os
import pep8



class TestConsole(unittest.TestCase):
    """This is Class to test the console"""

    @classmethod
    def setUpClass(cls_instance):
        """This is Function to set the variable for the console instance"""

        cls_instance.console = HBNBCommand()

    @classmethod
    def teardown(cls_instance):
        """This is Function deletes setup variables"""

        del cls_instance.console
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doc_strings(self):
        """This is Function see if doctrings are present"""

        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.update_dict.__doc__)

    def test_console_style(self):
        """This is Function that checks if the file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['console.py'])
        self.assertEqual(style.total_errors, 0, "not pep8")

    def test_test_console_style(self):
        """This is Function to check if the file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['tests/test_console.py'])
        self.assertEqual(style.total_errors, 0, "not pep8")

    def test_emptyline(self):
        """This is Function to test if there emptyline command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_quit(self):
        """This is Function that tests how the quit command works"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """This is Function that tests how create command works"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Mando")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            self.assertEqual('[]\n', f.getvalue()[:7])

    def test_destroy(self):
        """This is Function to test the destroy command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy lgbt")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 419")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.destroy('419')")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_show(self):
        """This is function that Tests if cmd output: show"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("ShitClass.show()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show('419')")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_update(self):
        """This is Function that tests the update command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update phone")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 419")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 13")
            self.assertEqual("** no instance found **\n", f.getvalue())
            
    def test_cmd(self):
        """This is Function to test cmd"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.count()")
            self.assertEqual(int, type(eval(f.getvalue())))

    def test_all(self):
        """This is Function that tests all command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all something")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())

if __name__ == "__main__":
    unittest.main()
