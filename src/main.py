from mainmenu import MainMenu
from termcolor import cprint

def main():
    try:
        main_menu = MainMenu()
        main_menu.load_boss_records()

        while True:
            choice = main_menu.display()
            if choice == 1:
                main_menu.drop_calculator()
            elif choice == 2:
                main_menu.simulate_attempts()
            elif choice == 3:
                main_menu.store_boss_stats()
            elif choice == 4:
                main_menu.display_boss_stats()
            elif choice == 5:
                main_menu.exit_program()
            else:
                cprint('Invalid choice. Please enter a number from 1 to 5.', 'red', attrs=['bold'])
                
    except Exception as exception:
        print("An unexpected error occured:", str(exception))

if __name__ == "__main__":
    main()


