#!/usr/bin/env python3
"""
create a unit test from an existing python
module
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    create testcase for module
    """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nest_map, path, expected):
        # test access_nested_map using parameterized
        self.assertEqual(access_nested_map(nest_map, path), expected)


if __name__ == '__main__':
    unittest.main()
