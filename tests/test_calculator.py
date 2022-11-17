import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding(self):
        assert self.calc.adding(1, 2) == 3, 'Should be 3'

    def test_substraction(self):
        assert self.calc.subtraction(7, 2) == 5, 'Should be 5'

    def test_multiply(self):
        assert self.calc.multiply(5, 3) == 15, 'Should be 15'

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_division(self):
        assert self.calc.division(8, 4) == 2, 'Should be 2'

    def teardown(self):
        print('\nВыполнение метода Teardown', end='')