def safe_input(prompt, conversion_func=None):
        readable_error = {
            'int': 'numbers',
            'float': 'numbers',
            'str': 'text'
        }

        while True:
            user_input = input(prompt)
            if user_input.lower() == "exit":
                exit()
            # elif user_input.lower() == "menu":
            #     display()
            elif conversion_func:
                try:
                    converted = conversion_func(user_input)
                    if isinstance(converted, int) or isinstance(converted, float):
                        if user_input.isnumeric():
                            return converted
                        else:
                            print(f"Invalid input! - Please enter {readable_error[conversion_func.__name__]}.")
                    else:
                        if user_input.isalpha():
                            return converted
                        else: print(f"Invalid input! - Please enter {readable_error[conversion_func.__name__]} without special characters or numbers.")
                except ValueError:
                    print(f"Invalid input! - Please enter {readable_error[conversion_func.__name__]}.")
            else:
                return user_input