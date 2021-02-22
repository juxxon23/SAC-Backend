import unittest
from test.unit.user.test_login import TestLogin

suite = unittest.TestSuite()
suite.addTest(TestLogin("test_access"))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
