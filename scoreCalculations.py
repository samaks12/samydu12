import unittest
from testScore import *

class MyFirstTests(unittest.TestCase):

    def test_ScoreCalculations(self):
        self.assertEqual(ScoreCal('Joseph', 15), '66%')

    #def ScoreCalculations(self):
        #self.assertEqual(scoreCal(name, age), '50%')

    #def ScoreCalculations(self):
        #self.assertEqual(scoreCal(name,age), '43%')

    #def ScoreCalculations(self):
        #self.assertEqual(scoreCal(name,age), '75%')
