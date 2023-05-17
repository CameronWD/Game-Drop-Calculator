import random
from tqdm import tqdm
from termcolor import cprint
from inpututil import safe_input

class AttemptSimulator:
    def __init__(self, main_menu):
        self.menu = main_menu

    def calculate(self):
        boss_name = safe_input("Boss name:\n")

        while True:
            drop_rate = safe_input("Drop rate (e.g. 0.01 for 1/100 or 100 for 1/100):\n", float)
            if drop_rate == 1:
                print("Drop rate cannot be 1. Please enter a decimal or a whole number.")
                continue
            else:
                if drop_rate > 1:
                    drop_rate = 1 / drop_rate
                break

        while True:
            simulated_successful_occurrences = safe_input("Simulated successful occurrences (1-100000000):\n", int)
            if simulated_successful_occurrences <= 0:
                print("Invalid input for simulated successful occurrences. Please enter a positive whole number.")
            else:
                break

        attempts_per_success = []
        for simulation in tqdm(range(simulated_successful_occurrences)):
            attempts = 0
            while random.random() >= drop_rate:
                attempts += 1
            attempts_per_success.append(attempts)

        min_attempts = min(attempts_per_success)
        max_attempts = max(attempts_per_success)
        avg_attempts = sum(attempts_per_success) / len(attempts_per_success)

        cprint(f"Program successfully got the drop {simulated_successful_occurrences} times from {boss_name}.", 'light_cyan')
        cprint(f"The fewest attempts between drops was {min_attempts} and the most was {max_attempts}.", 'light_cyan')
        cprint(f"Average attempts to be successful was: {avg_attempts:.3f}", 'light_cyan')
        safe_input("Press any key to return to main menu\n")

