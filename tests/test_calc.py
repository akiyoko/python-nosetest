import nose
from nose.tools import raises, assert_true, assert_equal, assert_raises

import calc


class TestCalculator(object):

    def setup(self):
        self.calculator = calc.Calculator(2)

    def test_add_when_arg_is_int(self):
        expected = 3
        actual = self.calculator.add(1)
        assert_equal(expected, actual)

    def test_add_when_arg_is_float(self):
        expected = 3.1
        actual = self.calculator.add(1.1)
        assert_equal(expected, actual)

    @raises(TypeError)
    def test_add_when_arg_is_str(self):
        self.calculator.add('1')

    def test_add_when_arg_is_none(self):
        with assert_raises(Exception) as em:
            self.calculator.add(None)
        e = em.exception
        assert_equal("Arg should not be None.", str(e))
