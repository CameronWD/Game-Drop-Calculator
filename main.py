from mainmenu import MainMenu
from DropCalculator import DropCalculator

def main():
    try:
        main_menu = MainMenu()
        main_menu.load_boss_records()
        calculate = DropCalculator()

        while True:
            choice = main_menu.display()
            if choice == 1:
                calculate.calculate()
            elif choice == 2:
                main_menu.simulate_attempts()
            elif choice == 3:
                main_menu.store_boss_stats()
            elif choice == 4:
                main_menu.display_boss_stats()
            elif choice == 5:
                main_menu.exit_program()
            else:
                print('Invalid choice. Please enter a number from 1 to 5.')
    except Exception as e:
        print("An unexpected error occured: ", str(e))

if __name__ == "__main__":
    main()


