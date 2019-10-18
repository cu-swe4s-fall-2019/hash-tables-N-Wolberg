import unittest
import os
import datetime
import hash_functions
import hash_tables


class TestHash(unittest.TestCase):
    def test_h_ascii(self):
        a = hash_functions.h_ascii('ACT', 1000)
        b = hash_functions.h_ascii('CAT', 1000)
        self.assertEqual(a, b)
        a = hash_functions.h_ascii('AAA', 'a')
        self.assertEqual(a, None)
        a = hash_functions.h_ascii('123', 1000)
        self.assertEqual(a, 150)

    def test_h_rolling(self):
        a = hash_functions.h_rolling('AB', 1000)
        b = hash_functions.h_rolling('BA', 1000)
        self.assertNotEqual(a, b)
        a = hash_functions.h_ascii('AAA', 'a')
        self.assertEqual(a, None)


if __name__ == '__main__':
    unittest.main()