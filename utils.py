



def request_user_input_int(prompt_msg):

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            int_input = int(user_input)
            valid = True
        except ValueError:
            print("Please enter an integer value.")

    return int_input


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



