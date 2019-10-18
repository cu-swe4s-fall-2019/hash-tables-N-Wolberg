import unittest
import os
import datetime
import hash_functions
import hash_tables


class TestHash(unittest.TestCase):

    def test_h_ascii(self):
        a = hash_functions.h_ascii_sum('ACT', 1000)
        b = hash_functions.h_ascii_sum('CAT', 1000)
        self.assertEqual(a, b)
        with self.assertRaises(TypeError) as ctx:
            hash_functions.h_ascii_sum(154, None)
        self.assertEqual(str(ctx.exception), 'First Argument Must Be A String')
        with self.assertRaises(TypeError) as ctx:
            hash_functions.h_ascii_sum("test", None)
        self.assertEqual(str(ctx.exception), 'Second Argument '
                                             'Must Be An Integer')

    def test_h_rolling(self):
        a = hash_functions.h_polynomial_rolling('AB', 1000)
        b = hash_functions.h_polynomial_rolling('BA', 1000)
        self.assertNotEqual(a, b)
        with self.assertRaises(TypeError) as ctx:
            hash_functions.h_polynomial_rolling(1234, None)
        self.assertEqual(str(ctx.exception), 'First Argument Must Be A String')
        with self.assertRaises(TypeError) as ctx:
            hash_functions.h_polynomial_rolling("test", None)
        self.assertEqual(str(ctx.exception), 'Second Argument '
                                             'Must Be An Integer')

    def test_linear_probing(self):
        t = hash_tables.LinearProbe(1000, hash_functions.h_ascii_sum)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
        # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)

        t = hash_tables.LinearProbe(1000, hash_functions.h_polynomial_rolling)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
        # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)

    def test_chained_hash(self):
        t = hash_tables.ChainedHash(1000, hash_functions.h_ascii_sum)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
        # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)

        t = hash_tables.ChainedHash(1000, hash_functions.h_polynomial_rolling)
        t.add('ACT', 10)
        t.add('123', 20)
        self.assertEqual(t.search('ACT'), 10)
        self.assertEqual(t.search('123'), 20)
        # search for the key that does not exist in the table
        self.assertEqual(t.search('nnn'), None)


if __name__ == '__main__':
    unittest.main()
