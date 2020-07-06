#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @IDE    ：PyCharm
# @Author ：Shen LI
# @Date   ：2020/7/6 10:50
import unittest
from demo import MyClass


class MyclassTest(unittest.TestCase):
    def setUp(self) -> None:
        self.clac = MyClass(4, 3)

    def tearDown(self) -> None:
        pass

    def test_add(self):
        ret = self.clac.add()
        self.assertEqual(ret, 7)

    def test_sub(self):
        ret = self.clac.sub()
        self.assertEqual(ret, 1)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_add'))
    suite.addTest(MyclassTest('test_sub'))

    runner = unittest.TextTestRunner()
    runner.run(suite)