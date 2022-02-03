import unittest
import random

class TestSimulateLogistics(unittest.TestCase):

    shared_resource = None

    @classmethod
    def setUpClass(cls):
        cls.shared_resource = random.randint(1, 100)

    @classmethod
    def tearDownClass(cls):
        cls.shared_resource = None

    def test_1(self):
        print('test 1:', self.shared_resource)

    def test_2(self):
        print('test 2:', self.shared_resource)

    def test_3(self):
        print('test 3:', self.shared_resource)
