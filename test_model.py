import unittest
from pollution_model import simulate
class ModelTests(unittest.TestCase):
    def test_scores(self):
        d=simulate();self.assertEqual(len(d['sensors']),12);self.assertAlmostEqual(sum(s['score'] for s in d['sources']),100,delta=.2)
    def test_wind(self):self.assertNotEqual(simulate()['sensors'],simulate(direction=180)['sensors'])
    def test_source(self):self.assertNotEqual(simulate()['sources'],simulate(source=1)['sources'])
    def test_repeat(self):self.assertEqual(simulate(),simulate())
if __name__=='__main__':unittest.main()
