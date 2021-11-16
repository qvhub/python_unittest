import unittest

from mon_module.function import add, divide, concatenation

class TestMonModule(unittest.TestCase):

    def test_add(self):
        # self.assertEquel(a,b) <-- verifie aue a == b
        self.assertEqual(add(5,4), 9)
        self.assertIsInstance(add(5,4), int)
    
    def test_divide(self):

        self.assertEqual(divide(10,2), 5)
        with self.assertRaises(Exception):
            divide(5,0)

    def test_concatenation(self):

        self.assertEqual(concatenation('mot', 'deux'), "motdeux")
        self.assertIsInstance(concatenation('mot', 'deux'), str)
        
        with self.assertRaises(TypeError):
            concatenation('mot',6)


if __name__ == "__main__":
    unittest.main()
