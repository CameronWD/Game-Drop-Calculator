class DisplayBossStats:
    @staticmethod
    def execute(menu):
        for boss in menu.boss_records.values():
            print(f"\nBoss: {boss.name}, Kill count: {boss.kill_attempts}, Total drops: {sum(item['count'] for item in boss.items_dropped.values())}")
            for item, details in boss.items_dropped.items():
                print(f"Item dropped: {item} - {details['count']}, Drop rate: {details['drop_rate']}")
        input("\nPress any key to return to the main menu\n")
        