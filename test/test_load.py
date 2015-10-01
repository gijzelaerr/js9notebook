import unittest
import js9notebook


class TestLoad(unittest.TestCase):
    def test_load(self):
        js9notebook.initialize()
