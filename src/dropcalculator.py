from termcolor import cprint
from inpututil import safe_input

class DropCalculator:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.boss_name = None
        self.drop_rate = None
        self.attempts = None
        self.success_probability = None

    def calculate(self):
        self.boss_name = safe_input("Enter boss name:\n")
        if self.boss_name is None: 
            return

        self.drop_rate = safe_input("Enter drop rate (e.g. 0.01 or 100 for a 1/100 chance):\n", float)
        if self.drop_rate is None: 
            return
        if float(self.drop_rate) > 1:
            self.drop_rate = 1 / float(self.drop_rate)

        self.attempts = safe_input("Enter number of attempts:\n", int)
        if self.attempts is None: 
            return

        self.success_probability = 1 - (1 - self.drop_rate) ** self.attempts
        cprint(f'There is a {self.drop_rate * 100:.3f}% chance per kill to receive the drop you want from {self.boss_name}', 'light_green')
        cprint(f'After {self.attempts} attempts, you had a {self.success_probability * 100:.3f}% chance of being successful at least once.', 'light_green')
        safe_input("Press any key to return to main menu\n")

        
