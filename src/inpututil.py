from art import aprint
from termcolor import cprint

def safe_input(prompt, conversion_func=None):
    readable_error = {
        'int': 'numbers',
        'float': 'numbers',
        'str': 'text'
    }

    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            cprint("Thank you for using Drop Chance Calculator!", "cyan")
            aprint("sad and confused")
            exit()  
        elif conversion_func:
            try:
                converted = conversion_func(user_input)
                if isinstance(converted, int) or isinstance(converted, float):
                    if user_input.replace('.','',1).isdigit():
                        if converted <= 0:
                            raise ValueError(f"Invalid input! - Please enter positive {readable_error[conversion_func.__name__]}.")
                        return converted
                    else:
                        cprint(f"Invalid input! - Please enter positive {readable_error[conversion_func.__name__]}.", "yellow")
            except ValueError as exception:
                cprint(f"Invalid input! - Please enter positive {readable_error[conversion_func.__name__]}.", "yellow")
        else:
            return user_input
