import unittest
import json
import os

from mon_module.analyzer import Analyzer

class TestMonModule(unittest.TestCase):

    def setUp(self):
        self.path = './json_classes.json'
        self.analyzer = Analyzer([0.4, 0.5, 0.4, 0.9, 0.5], 0.3, self.path)

        json_classes = {
                    0:"classe_1",
                    1:"classe_2",
                    2:"classe_3",
                    3:"classe_4",
                    4:"classe_5"
                    }

        with open(self.path, 'w') as fille:
            json.dump(json_classes, fille)
    
    def test_get_best_result(self):
        self.assertEqual(self.analyzer.get_best_result(), 0.9)

    def test_get_results(self):
        self.assertEqual(self.analyzer.get_results(), 3)
    
    def test_read_classes(self):
        self.assertEqual(self.analyzer.read_classes(), 'classe_4')
    
    def tearDown(self):
        os.remove(self.path)
        print("Nettoyage a la fin du test")
    

if __name__ == "__main__":
    unittest.main()
