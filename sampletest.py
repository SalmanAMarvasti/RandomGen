import unittest
import RandomSequence
class TestStringMethods(unittest.TestCase):

    def test_rand_gen(self):
        r = RandomSequence.RandomGen([-1, 0, 1, 2, 3] , [0.01, 0.3, 0.58, 0.1, 0.01], 21312414124)
        d = dict.fromkeys(r._random_nums, 0)
        for i in range(100):
            d[r.next_num()]+=1

        self.assertGreater(d[1], d[0])
        self.assertGreater(d[1], d[2])
        self.assertGreater(d[0], d[3])

    def test_extreme(self):
        r = RandomSequence.RandomGen([-1, 0, 1, 2, 3], [0.0, 0.0, 0.0, 0.99, 0.01], 21312414124 )
        d = dict.fromkeys(r._random_nums, 0)
        for i in range(100):
            d[r.next_num()] += 1
        print(d) # todo test extreme
        self.assertEqual(d[2],100)

    def test_empty(self):

        try:
            r = RandomSequence.RandomGen([], [])
            r.next_num()
        except ValueError:
            self.assertEqual(True, True)

    def test_normalization(self):
        r = RandomSequence.RandomGen([1, 2],[0.2, 0.5])
        try:
            r.normalise_sum(r._probabilities)
            self.assertGreaterEqual(r.normalise_sum(r._probabilities), RandomSequence.RandomGen.ONE)
        except ValueError:
            self.fail()


if __name__ == '__main__':
    unittest.main()