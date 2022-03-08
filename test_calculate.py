import unittest 
import SimpleCalculator

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator.Calculate()
    def test_add_method_returns_correct(self):
        self.assertEqual(4, self.calc.add(2,2))
    

if __name__ == '__main__':
    unittest.main()

