



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




