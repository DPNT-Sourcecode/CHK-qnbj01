import unittest
from lib.solutions.CHK.checkout_solution import checkout

class TestCheckout(unittest.TestCase):

    def test_checkout(self):
        self.assertEqual(checkout(""), 0)
        self.assertEqual(checkout("A"), 50)
        self.assertEqual(checkout("B"), 30)
        self.assertEqual(checkout("C"), 20)
        self.assertEqual(checkout("D"), 15)
        self.assertEqual(checkout("E"), 40)
        self.assertEqual(checkout("a"), -1)
        self.assertEqual(checkout("-"), -1)
        self.assertEqual(checkout("ABCa"), -1)
        self.assertEqual(checkout("AxA"), -1)
        self.assertEqual(checkout("ABCDE"), 155)
        self.assertEqual(checkout("AA"), 100)
        self.assertEqual(checkout("AAA"), 130)
        self.assertEqual(checkout("AAAA"), 180)
        self.assertEqual(checkout("AAAAA"), 200)
        self.assertEqual(checkout("AAAAAA"), 250)
        self.assertEqual(checkout("AAAAAAA"), 300)
        self.assertEqual(checkout("AAAAAAAA"), 330)
        self.assertEqual(checkout("AAAAAAAAA"), 380)
        self.assertEqual(checkout("AAAAAAAAAA"), 400)
        self.assertEqual(checkout("EE"), 80)
        self.assertEqual(checkout("EEB"), 80)
        self.assertEqual(checkout("EEEB"), 120)
        self.assertEqual(checkout("EEEEBB"), 160)
        self.assertEqual(checkout("BEBEEE"), 160)
        self.assertEqual(checkout("BB"), 45)
        self.assertEqual(checkout("BBB"), 75)
        self.assertEqual(checkout("BBBB"), 90)
        self.assertEqual(checkout("ABCDEABCDE"), 280)
        self.assertEqual(checkout("CCADDEEBBA"), 280)
        self.assertEqual(checkout("AAAAAEEBAAABB"), 455)

if __name__ == '__main__':
    unittest.main()
