from unittest import TestCase, main
from trades.trades_logic import *

class Tester(TestCase):
    def test_initArr(self):
        self.assertEqual(initArr('test_trade.csv'),
                         [])
