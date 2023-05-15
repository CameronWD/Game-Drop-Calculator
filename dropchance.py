def drop_chance():
    drop_rate = input("Enter drop rate (e.g. 0.01 or 100 for 1/100):\n")
    try:
        drop_rate = float(drop_rate)
        if drop_rate >= 1:
            drop_rate = 1 / drop_rate
    except ValueError:
        print("Error. Please only enter a whole number or a decimal. e.g 0.01 or 100 for 1/100")
        return

    boss_name = input("Enter boss name:\n")
    attempts = int(input("Enter number of attempts:\n"))
    item_name = input("Enter item name:\n")
    success_probability = 1 - (1 - drop_rate) ** attempts
    print(f'You have a {drop_rate * 100:.3f}% chance per kill to receive {item_name} from {boss_name}')
    print(f'After {attempts} attempts, you have a {success_probability * 100:.3f}% chance of being successful at least once.')
    input("Press any key to return to main menu\n")