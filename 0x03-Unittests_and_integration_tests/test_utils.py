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

    @parameterized.expand([
        ({}, ["a"], KeyError("a")),
        ({"a": 1}, ["a", "b"], KeyError("b"))
    ])
    def test_access_nested_map_exception(self, nest_map, path, expected):
        # Check for errors
        with self.assertRaises(KeyError) as error:
            access_nested_map(nest_map, path)

        self.assertEqual(str(error.exception), str(expected))


if __name__ == '__main__':
    unittest.main()
