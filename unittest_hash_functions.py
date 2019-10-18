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

    def test_linear_probing(self):
        t = hash_tables.LinearProbe(1000, hash_functions.h_ascii)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
        # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)

        t = hash_tables.LinearProbe(1000, hash_functions.h_rolling)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
         # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)

    def test_chained_hash(self):
        t = hash_tables.ChainedHash(1000, hash_functions.h_ascii)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
         # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)

        t = hash_tables.ChainedHash(1000, hash_functions.h_rolling)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
         # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)

if __name__ == '__main__':
    unittest.main()