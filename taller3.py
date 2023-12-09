import unittest
import numpy as np
from data_taller3.channels import A, B, C
from arrays import Arrays

class MyTestCase1(unittest.TestCase):

    def setUp(self):
        self.arr = Arrays()
        self.arr.fill_array(1, A, B, C)
        self.arr.fill_initial_table_for_taller3()

    def test(self):
        """ (A t+1 | ABC = 101) """
        distribution = self.arr.get_probability_distribution(
                        current_state=(1, 0, 1),
                        next_state=(True, None, None))
        
        distribution_format = [ round(i, 6) for i in distribution ]
        self.assertListEqual(distribution_format, [0.671429, 0.328571])

    def test2(self):
        """ (C t+1 | A = 0) """
        distribution = self.arr.get_probability_distribution(
                        current_state=(0, None, None),
                        next_state=(None, None, True))
        
        distribution_format = [ round(i, 6) for i in distribution ]
        self.assertListEqual(distribution_format, [0.757212, 0.242788])

    def test3(self):
        """ (AB t+1 | AB = 10) """
        distribution = self.arr.get_probability_distribution(
                        current_state=(1, 0, None),
                        next_state=(True, True, None))
        
        distribution_format = [ round(i, 6) for i in distribution ]
        self.assertListEqual(distribution_format, [0.281905, 0.422857, 0.118095, 0.177143])

