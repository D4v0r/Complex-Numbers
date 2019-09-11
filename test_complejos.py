import unittest
import complejos

class Test_complejos(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(complejos.suma((1, 2), (3, 4)), (4, 6))
    

if __name__ == "__main__":
    unittest.main()
