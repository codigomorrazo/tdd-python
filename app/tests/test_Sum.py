from unittest import TestCase

from app.src.Application.Sum import Sum


class TestSum(TestCase):
    def testMustFailIfParamsAreNotInt(self) -> None:
        sum = Sum()
        self.assertRaises(TypeError, sum.execute, 'blabla', 'lolo')
