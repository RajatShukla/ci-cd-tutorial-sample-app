import os
import sys
import unittest

import json

# Add parent directory to path for import
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from app import app, db
from app.models import Menu

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_DB = os.path.join(BASE_DIR, 'test.db')


class BasicTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_home(self):
        pass

    def test_menu_empty(self):
        pass

    def test_menu_item(self):
        pass

if __name__ == "__main__":
    unittest.main()
    print("Hello")
