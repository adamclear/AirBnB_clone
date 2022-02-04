#!/usr/bin/pyton3
"""
This module is the unittest for console.py
"""
import unittest
import pep8
import console
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):
    """
    This is the class for testing the console.
    """
    con = console.HBNBCommand()

    def setUp(self):
        """
        Setup class.
        """
        pass

    def tearDown(self):
        """
        Teardown class.
        """
        pass

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)
        # Method docstrings
        self.assertTrue(len(HBNBCommand.do_quit.__doc__) >= 1)
        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) >= 1)
        self.assertTrue(len(HBNBCommand.do_create.__doc__) >= 1)
        self.assertTrue(len(HBNBCommand.do_show.__doc__) >= 1)
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) >= 1)
        self.assertTrue(len(HBNBCommand.do_all.__doc__) >= 1)

    def test_quit(self):
        """
        Testing quit.
        """
        self.assertRaises(SystemExit, quit)

    def test_EOF(self):
        """
        Testing EOF.
        """
        with self.assertRaises(SystemExit):
            self.con.do_EOF()

    def test_empty_line(self):
        """
        Testing empty line.
        """
        empty_line_display = ''
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.emptyline()
            self.assertEqual(disp.getvalue(), empty_line_display)

    def test_create(self):
        """
        Testing create.
        """
        # No argument
        class_missing_display = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_create('')
            self.assertEqual(disp.getvalue(), class_missing_display)
        # Invalid Argument
        not_exist_display = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_create('NotBaseModel')
            self.assertEqual(disp.getvalue(), not_exist_display)
        # Works as intended
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_create('BaseModel')
            self.assertNotEqual(disp.getvalue(), class_missing_display)
            self.assertNotEqual(disp.getvalue(), not_exist_display)

    def test_show(self):
        """
        Testing show.
        """
        # No argument
        class_missing_display = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_show('')
            self.assertEqual(disp.getvalue(), class_missing_display)
        # No ID
        id_missing_display = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_show('BaseModel')
            self.assertEqual(disp.getvalue(), id_missing_display)
        # Invalid class
        invalid_class_display = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_show('notBaseModel')
            self.assertEqual(disp.getvalue(), invalid_class_display)
        # Invalid ID
        inst_not_found_disp = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_show('BaseModel yep')
            self.assertEqual(disp.getvalue(), inst_not_found_disp)
        # Working properly
        self.User1 = BaseModel(id='yep')
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_show('BaseModel yep')
            self.assertNotEqual(disp.getvalue(), class_missing_display)
            self.assertNotEqual(disp.getvalue(), id_missing_display)
            self.assertNotEqual(disp.getvalue(), invalid_class_display)
            self.assertNotEqual(disp.getvalue(), inst_not_found_disp)

    def test_destroy(self):
        """
        Testing destroy.
        """
        # No argument
        class_missing_display = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_destroy('')
            self.assertEqual(disp.getvalue(), class_missing_display)
        # No ID
        id_missing_display = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_destroy('BaseModel')
            self.assertEqual(disp.getvalue(), id_missing_display)
        # Invalid class
        invalid_class_display = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_destroy('notBaseModel')
            self.assertEqual(disp.getvalue(), invalid_class_display)
        # Invalid ID
        inst_not_found_disp = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_destroy('BaseModel yep')
            self.assertEqual(disp.getvalue(), inst_not_found_disp)
        # Working properly
        self.User1 = BaseModel(id='yep')
        with patch("sys.stdout", new=StringIO()) as disp:
            self.con.do_destroy('BaseModel yep')
            self.assertNotEqual(disp.getvalue(), class_missing_display)
            self.assertNotEqual(disp.getvalue(), id_missing_display)
            self.assertNotEqual(disp.getvalue(), invalid_class_display)
            self.assertNotEqual(disp.getvalue(), inst_not_found_disp)
        item_all = storage.all()
        if "BaseModel.yep" in item_all:
            result = False
        else:
            result = True
        self.assertEqual(result, True)
