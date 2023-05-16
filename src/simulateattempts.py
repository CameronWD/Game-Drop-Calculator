import random
from tqdm import tqdm
from termcolor import cprint
from inpututil import safe_input


class SimulateAttempts:

    def calculate():

        boss_name = safe_input("Boss name:\n")

        drop_rate = safe_input("Drop rate (e.g. 0.01 for 1/100 or 100 for 1/100):\n")
        try:
            drop_rate = float(drop_rate)
            if drop_rate > 1:
                drop_rate = 1 / drop_rate
        except ValueError:
            print("Invalid input for drop rate. Please enter a decimal or a whole number.")
            return

        simulated_successful_occurrences = int(input("Simulated successful occurrences (1-1000):\n"))
        
        attempts_per_success = []
        for _ in tqdm(range(simulated_successful_occurrences)):
            attempts = 0
            while random.random() >= drop_rate:
                attempts += 1
            attempts_per_success.append(attempts)

        min_attempts = min(attempts_per_success)
        max_attempts = max(attempts_per_success)
        avg_attempts = sum(attempts_per_success) / len(attempts_per_success)

#variable/private

        cprint(f"Program successfully got the drop {simulated_successful_occurrences} times from {boss_name}.", 'light_cyan')
        cprint(f"The fewest attempts between drops was {min_attempts} and the most was {max_attempts}.", 'light_cyan')
        cprint(f"Average attempts to be successful was: {avg_attempts:.3f}", 'light_cyan')
        safe_input("Press any key to return to main menu\n")
