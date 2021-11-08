from unittest import TestCase
from demo import Calc
#除法
# class testCalc(TestCase):
#
#     def testDev1(self):
#
#          a = 6
#          b = 3
#          c = 2
#
#          calc = Calc()
#          sum = calc.devision(a,b)
#
#          self.assertEqual(c,sum)

#乘法
# class testCalc(TestCase):
#
#      def testMuiti(self):
#           a = 6
#           b = 3
#           c = 18
#
#           calc = Calc()
#           sum = calc.multi(a,b)
#           self.assertEqual(c,sum)

#减法

class  testCalc(TestCase):
     def testSub(self):
          a = 6
          b = 3
          c = 3

          calc = Calc()
          sum = calc.subs(a,b)
          self.assertEqual(c,sum)
