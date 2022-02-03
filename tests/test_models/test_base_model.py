#!/usr/bin/python3
"""
This module is the unittest file for the class: BaseModel.
"""
from genericpath import exists
import unittest
from models.base_model import BaseModel
import pep8


class TestBaseClass(unittest.TestCase):
    """
    This class is for testing BaseModel.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.User1 = BaseModel()
        self.User2 = BaseModel()

    def tearDown(self):
        """
        Teardown method.
        """
        del self.User1
        del self.User2

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(BaseModel.__doc__) >= 1)
        # Method docstrings
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        # Test IDs
        self.assertTrue(self.User1.id, exists)
        self.assertTrue(type(self.User1.id) is str)
        self.assertNotEqual(self.User1.id, self.User2.id)
        # Test created datetime
        self.assertTrue(self.User1.created_at, exists)
        self.assertNotEqual(self.User1.created_at, self.User2.created_at)
        # Test updated datetime
        self.assertEqual(self.User1.created_at, self.User1.updated_at)

    def test_str(self):
        """
        Testing __str__.
        """
        expected_display = "[{}] ({}) {}".format(
                self.User1.__class__.__name__,
                self.User1.id,
                self.User1.__dict__)
        self.assertEqual(self.User1.__str__(), expected_display)

    def test_save(self):
        """
        Testing save.
        """
        self.User1.save()
        self.assertNotEqual(self.User1.created_at, self.User1.updated_at)

    def test_to_dict(self):
        """
        Testing to_dict.
        """
        User1_dict = self.User1.to_dict()
        self.assertEqual(User1_dict['__class__'], 'BaseModel')
        self.assertEqual(User1_dict['created_at'],
                         self.User1.created_at.isoformat())
        self.assertEqual(User1_dict['updated_at'],
                         self.User1.updated_at.isoformat())
        self.assertEqual(User1_dict['id'], self.User1.id)
        #test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.User1, 'NonExistentKey')
        #set attr and test it
        self.User1.Job = "Code Monkey"
        self.assertTrue(self.User1.Job, exists)


if __name__ == "__main__":
    unittest.main()
