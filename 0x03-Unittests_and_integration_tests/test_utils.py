#!/usr/bin/env python3
"""
create a unit test from an existing python
module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """
        implement a test json test case
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict):
        with patch('requests.get') as mock_url:
            mock_url.return_value.json.return_value = test_payload
            data = get_json(test_url)
            mock_url.assert_called_once()
            self.assertEqual(data, test_payload)


if __name__ == '__main__':
    unittest.main()
