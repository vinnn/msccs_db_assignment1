from datetime import datetime, timedelta
import re

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


def request_user_input_datetime(prompt_msg):

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            validated_input = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
            valid = True
        except ValueError:
            print("Please enter a valid date-time input.")

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



def request_user_input_name(prompt_msg):

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            any_invalid_char = False
            for c in user_input:
                if not (c.isalpha() or c==' ' or c== '-'):
                    any_invalid_char = True

            if not any_invalid_char:
                validated_input = user_input
                valid = True
            else:
                print("Please enter a valid name.")
        except ValueError:
            print("Please enter a valid name.")

    return validated_input



def request_user_input_email(prompt_msg):

    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            valid = bool(re.fullmatch(regex, user_input))
            if not valid:
                print("Please enter a valid email address.")
        except ValueError:
            print("Please enter a valid email address.")

    return user_input


def request_user_input_phone(prompt_msg):

    valid = False
    while not valid:
        user_input = input(prompt_msg)
        try:
            valid = user_input.isdigit() and 8 <= len(user_input) <= 16
            if not valid:
                print("Please enter a valid phone number (only digits, length between 8 and 16).")
        except ValueError:
            print("Please enter a valid phone number (only digits, length between 8 and 16).")

    return user_input



def add_duration_to_datetime(datetime0_str=None, duration_str=None):
    '''
    adds a duration expressed as "HH:MM:SS" to a datetime
    returns the resulting datetime
    https://stackoverflow.com/questions/19234771/adding-a-timedelta-of-the-type-hh-mm-ss-ms-to-a-datetime-object
    '''

    try:
        datetime0_dt = datetime.strptime(datetime0_str, "%Y-%m-%d %H:%M:%S")
        duration_dt = datetime.strptime(duration_str, "%H:%M:%S")
        # duration_dt.hour
        # duration_dt.minute

        delta_dt = timedelta(hours=duration_dt.hour, minutes=duration_dt.minute)

        datetime1_dt = datetime0_dt + delta_dt

        datetime1_str = datetime1_dt.strftime("%Y-%m-%d %H:%M:%S")

        print(datetime0_str)
        print(duration_str)
        print(datetime1_str)

        return datetime1_str
    
    except ValueError:
        return None



