import unittest
import całki
import horner_algorithm
import quick_incitement
import sqrt_algoritm
import zero_place

class Test(unittest.TestCase):
    def test_horner(self):
        self.assertEqual(horner_algorithm.horner(3,4,[3,4,-5,6,1]),325)

    def test_sqrt(self):
        self.assertEqual(round(sqrt_algoritm.sqrt(17,0.01),2),4.12)
        self.assertEqual(round(sqrt_algoritm.sqrt(19,0.01),2),4.36)
    def test_zeroplace(self):
        self.assertEqual(round(zero_place.zero_place(0.1),2),7.73)

    def test_quickIncitement(self):
        self.assertEqual(quick_incitement.incitement(6,2),36)
        self.assertEqual(quick_incitement.incitement(8,2),64)
        self.assertEqual(quick_incitement.incitement(2,4),16)
        self.assertEqual(quick_incitement.incitement(2,5),32)
