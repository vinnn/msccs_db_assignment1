from datetime import datetime, timedelta
import re

def request_user_input_int(prompt_msg):
    '''
    checks if the user input is an integer
    if not, prompt the user to enter a new input
    '''
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
    '''
    checks if the user input is included in the list 'in_list_str'
    if not, prompt the user to enter a new input
    '''
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
    '''
    checks if the user input is in datetime format
    if not, prompt the user to enter a new input
    '''
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
    '''
    checks if the user input is in a date format
    if not, prompt the user to enter a new input
    '''
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
    '''
    checks if the user input is in time format
    if not, prompt the user to enter a new input
    '''
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
    '''
    checks if the user input is in a person's name format (ie combination of characters, spaces and potentially dashes)
    if not, prompt the user to enter a new input
    '''
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
    '''
    checks if the user input is in an email format
    if not, prompt the user to enter a new input
    '''
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
    '''
    checks if the user input is in a phone format
    if not, prompt the user to enter a new input
    '''
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



