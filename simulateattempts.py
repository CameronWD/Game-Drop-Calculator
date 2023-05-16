import random
from tqdm import tqdm

class SimulateAttempts:
    @staticmethod
    def calculate():
        drop_rate = input("Drop rate (e.g. 0.01 for 1/100 or 100 for 1/100):\n")
        # Convert input to float if in decimal format, otherwise calculate inverse
        try:
            drop_rate = float(drop_rate)
            if drop_rate > 1:
                drop_rate = 1 / drop_rate
        except ValueError:
            print("Invalid input for drop rate. Please enter a decimal or a whole number.")
            return

        boss_name = input("Boss name:\n")
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

        print(f"Program successfully got the drop {simulated_successful_occurrences} times.")
        print(f"The fewest attempts it took was {min_attempts} and the most attempts was {max_attempts}.")
        print(f"Average attempts to be successful was: {avg_attempts:.3f}")
        input("Press any key to return to main menu\n")
