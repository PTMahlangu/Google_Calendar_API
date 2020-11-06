
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from config import config
import os.path
from os import path

class TestFunctions(unittest.TestCase):
    
    def test_connection_status(self):
        service,status =config()
        self.assertEqual(201,status)

    def test_if_file_exist_1(self):
        self.assertTrue(path.exists('.credentials.json'))

    def test_if_file_exist_2(self):
        self.assertTrue(path.exists('.token.pickle'))

