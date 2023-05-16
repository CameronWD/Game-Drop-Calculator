
# from mainmenu import MainMenu
from termcolor import cprint
from inpututil import safe_input


class DropCalculator:
    def __init__(self, MainMenu):
        self.menu = MainMenu

    def calculate(self):
        boss_name = safe_input("Enter boss name:\n")
        if boss_name is None: return

        drop_rate = safe_input("Enter drop rate (e.g. 0.01 or 100 for a 1/100 chance):\n", float)
        if drop_rate is None: return
        if drop_rate > 1:
            drop_rate = 1 / drop_rate

        attempts = safe_input("Enter number of attempts:\n", int)
        if attempts is None: return

        success_prob = 1 - (1 - drop_rate) ** attempts
        cprint(f'There is a {drop_rate * 100:.3f}% chance per kill to receive the drop you want from {boss_name}', 'light_green')
        cprint(f'After {attempts} attempts, you had a {success_prob * 100:.3f}% chance of being successful at least once.', 'light_green')
        input("Press any key to return to main menu\n")
