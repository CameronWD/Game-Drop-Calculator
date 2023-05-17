import json
import unittest
from unittest.mock import patch
from dropcalculator import DropCalculator
from unittest.mock import patch, MagicMock, mock_open
from mainmenu import MainMenu

def test_drop_calculator_correct_input(monkeypatch):
    inputs = iter(['Boss name', 100, 100, ''])
    monkeypatch.setattr('dropcalculator.safe_input', lambda prompt, conversion_func=None: next(inputs, ''))
    main_menu = None
    drop_calculator = DropCalculator(main_menu)

    drop_calculator.calculate()

    assert drop_calculator.boss_name == 'Boss name'
    assert drop_calculator.drop_rate == 0.01
    assert drop_calculator.attempts == 100

def test_drop_calculator_correct_result(monkeypatch):
    inputs = iter(['Boss name', 100, 100, ''])
    monkeypatch.setattr('dropcalculator.safe_input', lambda prompt, conversion_func=None: next(inputs, ''))
    main_menu = None
    drop_calculator = DropCalculator(main_menu)
    drop_calculator.calculate()

    assert drop_calculator.success_probability == 0.6339676587267709

@patch('mainmenu.cprint')
@patch('mainmenu.open', new_callable=mock_open)
@patch('mainmenu.json')
@patch('mainmenu.BossStore')

def test_load_boss_records(MockBossStore, MockJson, MockOpen, MockCprint):
    MockOpen.side_effect = [FileNotFoundError(), MagicMock()]
    MockJson.load.side_effect = json.decoder.JSONDecodeError

    main_menu = MainMenu()
    main_menu.load_boss_records()

    MockCprint.assert_any_call("boss_stats.json not found. Creating a new file now.", "red", attrs=["bold"])


@patch('mainmenu.safe_input')
def test_display(MockSafeInput):
    MockSafeInput.return_value = 1

    main_menu = MainMenu()
    result = main_menu.display()

    assert result == 1


if __name__ == '__main__':
    unittest.main()
