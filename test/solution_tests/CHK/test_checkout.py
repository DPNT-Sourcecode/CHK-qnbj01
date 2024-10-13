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
        self.assertEqual(checkout("F"), 10)
        self.assertEqual(checkout("G"), 20)
        self.assertEqual(checkout("H"), 10)
        self.assertEqual(checkout("I"), 35)
        self.assertEqual(checkout("J"), 60)
        self.assertEqual(checkout("K"), 80)
        self.assertEqual(checkout("L"), 90)
        self.assertEqual(checkout("M"), 15)
        self.assertEqual(checkout("N"), 40)
        self.assertEqual(checkout("O"), 10)
        self.assertEqual(checkout("P"), 50)
        self.assertEqual(checkout("Q"), 30)
        self.assertEqual(checkout("R"), 50)
        self.assertEqual(checkout("S"), 30)
        self.assertEqual(checkout("T"), 20)
        self.assertEqual(checkout("U"), 40)
        self.assertEqual(checkout("V"), 50)
        self.assertEqual(checkout("W"), 20)
        self.assertEqual(checkout("X"), 90)
        self.assertEqual(checkout("Y"), 10)
        self.assertEqual(checkout("Z"), 50)
        self.assertEqual(checkout("a"), -1)
        self.assertEqual(checkout("-"), -1)
        self.assertEqual(checkout("ABCa"), -1)
        self.assertEqual(checkout("AxA"), -1)
        self.assertEqual(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 965)
        self.assertEqual(checkout("AA"), 100)
        self.assertEqual(checkout("AAA"), 130)
        self.assertEqual(checkout("AAAA"), 180)
        self.assertEqual(checkout("AAAAA"), 200)
        self.assertEqual(checkout("AAAAAA"), 250)
        self.assertEqual(checkout("AAAAAAA"), 300)
        self.assertEqual(checkout("AAAAAAAA"), 330)
        self.assertEqual(checkout("AAAAAAAAA"), 380)
        self.assertEqual(checkout("AAAAAAAAAA"), 400)
        self.assertEqual(checkout("PP"), 100)
        self.assertEqual(checkout("PPP"), 150)
        self.assertEqual(checkout("PPPP"), 200)
        self.assertEqual(checkout("PPPPP"), 200)
        self.assertEqual(checkout("PPPPPP"), 250)
        self.assertEqual(checkout("PPPPPPP"), 300)
        self.assertEqual(checkout("PPPPPPPP"), 350)
        self.assertEqual(checkout("PPPPPPPPP"), 400)
        self.assertEqual(checkout("PPPPPPPPPP"), 400)
        self.assertEqual(checkout("UUU"), 120)
        self.assertEqual(checkout("UUUU"), 120)
        self.assertEqual(checkout("UUUUU"), 160)
        self.assertEqual(checkout("UUUUUUUU"), 240)
        self.assertEqual(checkout("EE"), 80)
        self.assertEqual(checkout("EEB"), 80)
        self.assertEqual(checkout("EEEB"), 120)
        self.assertEqual(checkout("EEEEBB"), 160)
        self.assertEqual(checkout("BEBEEE"), 160)
        self.assertEqual(checkout("RRR"), 150)
        self.assertEqual(checkout("RRRQ"), 150)
        self.assertEqual(checkout("RRRRQ"), 200)
        self.assertEqual(checkout("RRRRRRQQ"), 300)
        self.assertEqual(checkout("RRRQRQRR"), 300)
        self.assertEqual(checkout("H"), 10)
        self.assertEqual(checkout("HH"), 20)
        self.assertEqual(checkout("HHH"), 30)
        self.assertEqual(checkout("HHHH"), 40)
        self.assertEqual(checkout("HHHHH"), 45)
        self.assertEqual(checkout("HHHHHH"), 55)
        self.assertEqual(checkout("HHHHHHH"), 65)
        self.assertEqual(checkout("HHHHHHHH"), 75)
        self.assertEqual(checkout("HHHHHHHHH"), 85)
        self.assertEqual(checkout("HHHHHHHHHH"), 80)
        self.assertEqual(checkout("VV"), 90)
        self.assertEqual(checkout("VVV"), 130)
        self.assertEqual(checkout("VVVV"), 180)
        self.assertEqual(checkout("VVVVV"), 220)
        self.assertEqual(checkout("VVVVVV"), 260)
        self.assertEqual(checkout("NNN"), 120)
        self.assertEqual(checkout("NNNM"), 120)
        self.assertEqual(checkout("NNNNM"), 160)
        self.assertEqual(checkout("NNNNNNMM"), 240)
        self.assertEqual(checkout("NNNMNMNN"), 240)
        self.assertEqual(checkout("FF"), 20)
        self.assertEqual(checkout("FFF"), 20)
        self.assertEqual(checkout("FFFF"), 30)
        self.assertEqual(checkout("FFFFFF"), 40)
        self.assertEqual(checkout("K"), 80)
        self.assertEqual(checkout("KK"), 150)
        self.assertEqual(checkout("KKK"), 230)
        self.assertEqual(checkout("KKKK"), 300)
        self.assertEqual(checkout("QQ"), 60)
        self.assertEqual(checkout("QQQ"), 80)
        self.assertEqual(checkout("QQQQ"), 110)
        self.assertEqual(checkout("QQQQQ"), 140)
        self.assertEqual(checkout("QQQQQQ"), 160)
        self.assertEqual(checkout("VV"), 90)
        self.assertEqual(checkout("VVV"), 130)
        self.assertEqual(checkout("VVVV"), 180)
        self.assertEqual(checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH"), 1880)
        self.assertEqual(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), 1880)
        self.assertEqual(checkout("PPPPQRUVPQRUVPQRUVSU"), 740)
        self.assertEqual(checkout("AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHVVVBBNNNMFFFKKQQQVVHHHHH"), 1640)


if __name__ == '__main__':
    unittest.main()

