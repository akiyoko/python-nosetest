import random
from nose.tools import raises, assert_true, assert_equal, assert_raises


class TestSequenceFunctions(object):

    def setup(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        assert_equal(self.seq, range(10))

        # should raise an exception for an immutable sequence
        with assert_raises(TypeError):
            random.shuffle((1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        assert_true(element in self.seq)

    def test_sample(self):
        with assert_raises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            assert_true(element in self.seq)
