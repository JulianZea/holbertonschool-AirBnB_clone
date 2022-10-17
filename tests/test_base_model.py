#!/usr/bin/python3
"""Unittest for class BaseModel()
"""
import unittest
from models.base_model import BaseModel
import pycodestyle


class Test_Base(unittest.TestCase):

    def setUp(self):
        """ sets up"""
        self.baseModel = BaseModel()

    def test_doc(self):
        """Test docs"""
        self.assertIsNotNone(self.baseModel.__doc__)
        self.assertIsNotNone(self.baseModel.save.__doc__)
        self.assertIsNotNone(self.baseModel.to_dict.__doc__)

    def test_method(self):
        """Test methods"""
        self.assertTrue(hasattr(self.baseModel, "__init__"))
        self.assertTrue(hasattr(self.baseModel, "save"))
        self.assertTrue(hasattr(self.baseModel, "to_dict"))

    def test_save(self):
        """Test save"""
        pass

    def test_objects(self):
        """Test to_dict"""
        self.assertTrue(type(self.basemodel._objects), type([])) 
