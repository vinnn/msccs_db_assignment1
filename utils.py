from datetime import datetime



def request_user_input_int(prompt_msg):

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            validated_input = int(user_input)
            valid = True
        except ValueError:
            print("Please enter an integer value.")

    return validated_input


def request_user_input_in_list(prompt_msg, in_list_str):

    # user_input is a string type therefore convert elements of in_list as strings for comparison
    # in_list_str = [str(s) for s in in_list]

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            if user_input in in_list_str:
                validated_input = user_input
                valid = True
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("Please enter a valid input.")

    return validated_input



def request_user_input_date(prompt_msg):

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            validated_input = datetime.strptime(user_input, "%Y-%m-%d")
            valid = True
        except ValueError:
            print("Please enter a valid date input.")

    return validated_input



def request_user_input_time(prompt_msg):

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            validated_input = datetime.strptime(user_input, "%H:%M")
            valid = True
        except ValueError:
            print("Please enter a valid time input.")

    return validated_input