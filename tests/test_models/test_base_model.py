#!/usr/bin/python3

"""
    Unittests for BaseModel
"""

import unittest
import os
import pycodestyle
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4

class Test_BaseModel_Init(unittest.TestCase):
    """test the __init__"""

    def test_id_none(self):
        """Test id is not None"""
        base = BaseModel()
        self.assertIsNot(base.id, None)

    def test_class(self):
        """test the class name"""
        base = BaseModel()
        self.assertEqual(base.__class__.__name__, "BaseModel")

    def test_id_type(self):
        """test id str"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_id_length(self):
        """test the lenght id"""
        base = BaseModel()
        self.assertEqual(len(base.id), 36)

    def test_unique_created_at(self):
        """test created_at modif"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)

    def test_update_at_type(self):
        """test updated_at type"""
        base = BaseModel()
        self.assertEqual(type(base.updated_at), datetime)

    def test_created_at_updated(self):
        """test updated_at modif"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.updated_at)

    def test_different_updated_at(self):
        """test if updated_at change each time executed"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_kwargs(self):
        """test kwargs"""
        base = BaseModel()
        dict_a = base.to_dict()
        base2 = BaseModel(**dict_a)
        self.assertEqual(base.id, base2.id)

    def test_kwargs_class(self):
        """test kwargs class"""
        base = BaseModel()
        dict_a = base.to_dict()
        base2 = BaseModel(**dict_a)
        self.assertTrue(hasattr(base2, '__class__'))


class Test_BaseModel_Str(unittest.TestCase):
    """test the str method"""

    def test_representation_class_name_and_id(self):
        """test str representation"""
        base = BaseModel()
        base.id = 123
        self.assertTrue("[BaseModel] (123)", base.__str__)

    def test_representation_updated_at(self):
        """test update_at"""
        base = BaseModel()
        self.assertTrue('updated_at' in str(base), True)

    def test_representation_created_at(self):
        """test created_at"""
        base = BaseModel()
        self.assertTrue('created_at' in str(base), True)



class Test_BaseModel_Save(unittest.TestCase):
    """test the save method"""

    def test_name_base_model(self):
        """test save method with new str"""
        obj = BaseModel()
        obj.name = "Houssem"
        obj.save()
        self.assertEqual(obj.name, "Houssem")

    def test_save_update(self):
        """test update saved"""
        obj = BaseModel()
        obj.num = 1
        date1 = obj.updated_at
        obj.save()
        obj.num = 2
        date2 = obj.updated_at
        obj.save()
        self.assertNotEqual(date1, date2)

class Test_BaseModel_To_Dict(unittest.TestCase):
    """test the to_dict method"""

    def test_dictionary_return(self):
        """test the to_dict method"""
        base = BaseModel()
        my_dict = base.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_create_dictionary(self):
        """test to_dict"""
        base = BaseModel()
        self.assertEqual(type(base.__dict__), dict)

    def test_correct_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())


if __name__ == '__main__':
    unittest.main()
