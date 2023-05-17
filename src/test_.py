import pytest
from dropcalculator import DropCalculator
from termcolor import cprint
from inpututil import safe_input

# test_dropcalculator.py

def test(monkeypatch):
    inputs = iter(['Boss name', 100, 100, ''])
    monkeypatch.setattr('dropcalculator.safe_input', lambda prompt, conversion_func=None: next(inputs, ''))

    main_menu = None
    drop_calculator = DropCalculator(main_menu)

    drop_calculator.calculate()

    assert drop_calculator.boss_name == 'Boss name'
    assert drop_calculator.drop_rate == 0.01
    assert drop_calculator.attempts == 100
    assert drop_calculator.success_probability == 0.6339676587267709


def test_drop_calculator_input_error(monkeypatch):
    inputs = iter(['Boss name', 'abc', '100'])
    monkeypatch.setattr('dropcalculator.safe_input', lambda prompt, conversion_func=None: next(inputs, ''))

    main_menu = None 
    drop_calculator = DropCalculator(main_menu)

    with pytest.raises(ValueError):
        drop_calculator.calculate()




