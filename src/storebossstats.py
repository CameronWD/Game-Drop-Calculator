import json
from boss import BossStore
from inpututil import safe_input
from termcolor import cprint
class StoreBossStats:
    def __init__(self, MainMenu):
        self.main = MainMenu

    def execute(self):
        boss_name = safe_input("Boss name:\n")
        kill_attempts = int(safe_input("How many kill attempts do you have?\n"))
        items_dropped = {}
        while True:
            item_name = safe_input("Enter the name of the item dropped, or 'done' to finish:\n")
            if item_name.lower() == 'done':
                break
            item_drop_rate = float(safe_input("Enter the drop rate of the item:\n"))
            item_count = int(safe_input(f"How many times have you received {item_name}?\n"))
            items_dropped[item_name] = {'count': item_count, 'drop_rate': item_drop_rate}
        save = safe_input("Save? Y/N\n")
        if save.lower() == 'y':
            boss_instance = BossStore(boss_name, kill_attempts, items_dropped)
            self.main.boss_records[boss_name] = boss_instance
            with open('boss_stats.json', 'w') as file:
                json.dump({key: value.to_dict() for key, value in self.main.boss_records.items()}, file)
            cprint(f"Boss {boss_name} saved successfully.", "light_green")
        safe_input("Press any key to return to main menu\n")
        