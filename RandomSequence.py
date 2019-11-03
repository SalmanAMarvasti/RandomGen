
import random

# Salman Marvasti for AHL 2019
class RandomGen(object):
    # Values that may be returned by next_num()
   # _random_nums = []  # Probability of the occurence of random_nums
   # _probabilities = []  #
    ONE = 0.999
    def __init__(self, r , p, seed=0):
        if seed!=0:
            random.seed(seed)
        self._random_nums = r
        self._probabilities = p
        if len(self._probabilities) == 0:
            raise ValueError("Cannot return any number as prob are empty.")
        if len(self._probabilities) != len(self._random_nums):
            raise ValueError("Two lists must be the same lengths")

        if self.normalise_sum(self._probabilities)>0:
            self.prob_range = [0.0] * len(self._probabilities)
            self.prob_range[0] = self._probabilities[0]
            for i in range(1, len(self._probabilities)):
                self.prob_range[i] = self._probabilities[i] + self.prob_range[i-1]

    def next_num(self):
        rand = random.random()
        idx = self.find_in_range(rand, self.prob_range)
        return self._random_nums[idx]



    def find_in_range(self, n, prob_range):
        if prob_range[0] >= n:
            return 0

        for j in range(1, len(prob_range)):
            if prob_range[j] >= n:
                    return j
        return len(prob_range) - 1


    def normalise_sum(self, a):
        x = sum(a)
        if (x>1):
            return -1
        if (x>RandomGen.ONE): # assume epsilon of 1/1000
            return x
        self._probabilities = [y/x for y in self._probabilities]
        return 1.0