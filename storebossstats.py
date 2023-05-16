import json
from boss import Boss
from inpututil import safe_input

class StoreBossStats:
    @staticmethod
    def execute(main_menu):
        boss_name = safe_input("Boss name:\n")
        kill_attempts = int(input("How many kill attempts do you have?\n"))
        items_dropped = {}
        while True:
            item_name = safe_input("Enter the name of the item dropped, or 'done' to finish:\n")
            if item_name.lower() == 'done':
                break
            item_drop_rate = float(input("Enter the drop rate of the item:\n"))
            item_count = int(input(f"How many times have you received {item_name}?\n"))
            items_dropped[item_name] = {'count': item_count, 'drop_rate': item_drop_rate}
        save = safe_input("Save? Y/N\n")
        if save.lower() == 'y':
            boss_instance = Boss(boss_name, kill_attempts, items_dropped)
            main_menu.boss_records[boss_name] = boss_instance
            with open('boss_stats.json', 'w') as file:
                json.dump({key: value.to_dict() for key, value in main_menu.boss_records.items()}, file)
            print(f"Boss {boss_name} saved successfully.")
        safe_input("Press any key to return to main menu\n")
        