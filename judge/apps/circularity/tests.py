from __future__ import absolute_import
import unittest

from utils.build_tests import Package, build_test_suite

def test_suite():
    return build_test_suite(Package(__package__))


if __name__ == '__main__':
    # run tests
    runner = unittest.TextTestRunner()
    runner.run(test_suite())

