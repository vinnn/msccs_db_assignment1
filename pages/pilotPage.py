import os
from dbtables.pilotTable import PilotTable
from utils import request_user_input_in_list, request_user_input_name, request_user_input_email, request_user_input_phone, request_user_input_date

class PilotPage:

    ###############################################################################################################################
    def __init__(self):

        self.pilotTable = PilotTable()
        self.parentView = self.view_menu
        self.page_selected_datetime_from = None
        self.page_selected_datetime_to = None

    ###############################################################################################################################
    def view_menu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n*************************************************************")
        print("************************************************************* PILOT MENU")   
        print("*************************************************************")
        print("1. All pilots")
        print("2. Pilots available for period")
        print("3. Create new pilot")
        print("4. Statistics")        
        print("----------------------")
        print("0. to go back")  
        print("----------------------")

        __user_input = request_user_input_in_list(">>> Enter selection: ", ["0","1","2","3","4","M"])

        if __user_input == "0":
            return
        
        elif __user_input == "1":
            self.view_all_pilots()

        elif __user_input == "2":
            # user selected departure date:
            selected_datetime_from = request_user_input_date(">>> Enter period start date (YYYY-MM-DD): ")
            selected_datetime_to = request_user_input_date(">>> Enter period end date (YYYY-MM-DD): ")            
            if selected_datetime_from is not None and selected_datetime_to is not None:
                self.page_selected_datetime_from = selected_datetime_from #.strftime("%Y-%m-%d %H:%M:%S")
                self.page_selected_datetime_to = selected_datetime_to #.strftime("%Y-%m-%d %H:%M:%S")                
                self.view_pilots_available_in_period()
            else: 
                self.view_menu()

        elif __user_input == "3":
            self.view_create_pilot()

        elif __user_input == "4":
            self.view_stats()     
        else:
            print("Invalid Choice")   

    ###############################################################################################################################
    def view_all_pilots(self):
        '''
        display information for all pilots
        + prompt user to select one pilot for details or make changes
        '''
        self.parentView = self.view_all_pilots # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.pilotTable.select_all_pilots()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')  # clear screen before displaying page
            print("\n*************************************************************")
            print("************************************************************* ALL PILOTS")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<26}{:<26}{:<26}{:<14}"
            print(formatspecifier.format("id",
                                        "first name",
                                        "last name", 
                                        "email", 
                                        "phone"
                                        ))
            print("-" * 175)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["first_name"],                                                     
                                            row["last_name"], 
                                            row["email"], 
                                            row["phone"]
                                            ))
            print("-" * 175)

            # get list of pilot id options from the table (add "0" for 'go back' option):
            list_pilot_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select pilot id (0 to go back): ", list_pilot_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.view_details_one_pilot(int(__user_input))

        except Exception as e: # if exception, print + redirect to menu page
            print("Error : " + str(e))           
            self.view_menu() 

    ###############################################################################################################################
    def view_all_pilots_selection(self): 
        '''
        display all pilot options
        + prompt user to select an pilot id
        '''

        try:
            # get data from select query:
            data = self.pilotTable.select_all_pilots()

            # display extracted data as a table: 
            formatspecifier = "{:<6}{:<26}{:<26}{:<26}{:<14}"
            print(formatspecifier.format("id",
                                        "first name",
                                        "last name", 
                                        "email", 
                                        "phone"
                                        ))
            print("-" * 175)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["first_name"],                                                     
                                            row["last_name"], 
                                            row["email"], 
                                            row["phone"]
                                            ))
            print("-" * 175)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> Select pilot id (0 to go back): ", list_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                return None
            else:
                selected_pilot = [a for a in data if a["id"]==int(__user_input)][0]
                return selected_pilot

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            return None

    ###############################################################################################################################
    def view_pilots_available_in_period(self):
        '''
        display information for pilots available during the period [page_selected_datetime_from, page_selected_datetime_to]
        + prompt user to select one pilot for details or make changes
        '''
        self.parentView = self.view_pilots_available_in_period # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.pilotTable.select_all_pilots_available_by_period(self.page_selected_datetime_from, self.page_selected_datetime_to)

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')  # clear screen before displaying page
            print("\n*************************************************************")
            print("************************************************************* ALL PILOTS")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<26}{:<26}{:<26}{:<14}"
            print(formatspecifier.format("id",
                                        "first name",
                                        "last name", 
                                        "email", 
                                        "phone"
                                        ))
            print("-" * 175)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["first_name"],                                                     
                                            row["last_name"], 
                                            row["email"], 
                                            row["phone"]
                                            ))
            print("-" * 175)

            # get list of pilot id options from the table (add "0" for 'go back' option):
            list_pilot_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select pilot id (0 to go back): ", list_pilot_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.view_details_one_pilot(int(__user_input))

        except Exception as e: # if exception, print + redirect to menu page
            print("Error : " + str(e))           
            self.view_menu() 

    ###############################################################################################################################
    def view_details_one_pilot(self, pilot_id):
        '''
        display details for one pilot
        + menu for editing/deleting the pilot
        + prompt user for menu selection
        '''

        try:
            data = self.pilotTable.select_one_pilot(pilot_id)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n*************************************************************")
            print("************************************************************* PILOT DETAILS")   
            print("*************************************************************")
            print("{:<24}{:<24}\n".format("pilot id",data["id"]))
            print("{:<24}{:<24}".format("first name", data["first_name"]))            
            print("{:<24}{:<24}".format("last name", data["last_name"]))
            print("{:<24}{:<24}".format("email", data["email"]))
            print("{:<24}{:<24}".format("phone", data["phone"]))

            print("------------------------------------------------------------- Make changes:")  
            print("1. Change first name")
            print("2. Change last name")
            print("3. Change email")
            print("4. Change phone")
            print("5. Delete pilot")
            print("0. to go back")
            print("M. to main menu")
            print("----------------------")
            __user_input = request_user_input_in_list(">>> Enter selection: ", ["0","1","2","3","4","5","M"])

            if __user_input == "0":
                self.parentView() # go back to previous view

            elif __user_input == "M":
                self.view_menu() # go back to menu

            elif __user_input == "1":
                print(f"------------------------------------------------------------ Enter new first name: ")
                selected = request_user_input_name(">>> Enter new first name: ")

                print("replace with ", selected)
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.pilotTable.update_pilot(pilot_id, "first_name", selected)
                    print(update_status)
                    __ = input("(press Enter to refresh)") 
                    self.view_details_one_pilot(pilot_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)") 
                    self.view_details_one_pilot(pilot_id)

            elif __user_input == "2":
                print(f"------------------------------------------------------------ Enter new last name: ")
                selected = request_user_input_name(">>> Enter new last name: ")

                print("replace with ", selected)
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.pilotTable.update_pilot(pilot_id, "last_name", selected)
                    print(update_status)
                    __ = input("(press Enter to refresh)") 
                    self.view_details_one_pilot(pilot_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)") 
                    self.view_details_one_pilot(pilot_id)

            elif __user_input == "3":
                print(f"------------------------------------------------------------ Enter new email: ")
                selected = request_user_input_email(">>> Enter new email address: ")

                print("replace with ", selected)
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.pilotTable.update_pilot(pilot_id, "email", selected)
                    print(update_status)
                    __ = input("(press Enter to refresh)") 
                    self.view_details_one_pilot(pilot_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)") 
                    self.view_details_one_pilot(pilot_id)

            elif __user_input == "4":
                print(f"------------------------------------------------------------ Enter new phone: ")
                selected = request_user_input_phone(">>> Enter new phone number: ")

                print("replace with ", selected)
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.pilotTable.update_pilot(pilot_id, "phone", selected)
                    print(update_status)
                    __ = input("(press Enter to refresh)") 
                    self.view_details_one_pilot(pilot_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)") 
                    self.view_details_one_pilot(pilot_id)
            
            elif __user_input == "5":
                print(f"------------------------------------------------------------ Delete pilot:")
                __confirmation = request_user_input_in_list(">>> Confirm deletion ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    deletion_status = self.pilotTable.delete_pilot(pilot_id)
                    print(deletion_status)
                    __ = input("(press Enter)") 
                    self.parentView()  # go back to previous view
                else:
                    print("cancelled deletion")
                    __ = input("(press Enter)") 
                    self.view_details_one_pilot(pilot_id)            




        except Exception as e: # if exception, print + redirect to all flight menu page
            print("Error : " + str(e))   
            self.view_menu() 

    ###############################################################################################################################
    def view_available_pilots_by_period(self, from_datetime, to_datetime):
        '''
        display all pilots that are available during period
        '''

        try:
            # get data from select query:
            data = self.pilotTable.select_all_pilots_available_by_period(from_datetime, to_datetime)

            # print(data)

            formatspecifier = "{:<6}{:<20}{:<20}{:<30}{:<20}"
            print(formatspecifier.format("id", "first_name", "last_name", "email", "phone"))
            print("-" * 120)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["first_name"][:18], 
                                            row["last_name"][:18], 
                                            row["email"],
                                            row["phone"]
                                            ))
            print("-" * 120)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> Select pilot id (0 to go back): ", list_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                return
            else:
                selected_row = [a for a in data if a["id"]==int(__user_input)][0]
                return selected_row

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            # self.viewMenu() 

    # ###############################################################################################################################
    def view_create_pilot(self):
        '''
        display form for pilot creation
        '''
        self.parent_view = self.view_menu # to go back to this view when user goes back from detail view

        try:
            data = {}

            complete = False
            while not complete:
                os.system('cls' if os.name == 'nt' else 'clear')

                print("\n*************************************************************")
                print("************************************************************* NEW PILOT")   
                print("*************************************************************")

                print("{:<24}{:<24}".format("first name", data["first_name"] if "first_name" in data else ""))
                print("{:<24}{:<24}".format("last name", data["last_name"] if "last_name" in data else ""))
                print("{:<24}{:<24}\n".format("email address", data["email"] if "email" in data else ""))
                print("{:<24}{:<24}\n".format("phone no", data["phone"] if "phone" in data else ""))

                if "first_name" not in data:
                    print("------------------------------------------------------------- Enter first name:")  
                    selected = request_user_input_name(">>> Enter first name: ")
                    print("selected first name: ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["first_name"] = selected
                    else:
                        self.parent_view

                elif "last_name" not in data:
                    print("------------------------------------------------------------- Enter last name:")  
                    selected = request_user_input_name(">>> Enter last name: ")
                    print("selected last name: ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["last_name"] = selected
                    else:
                        self.parent_view

                elif "email" not in data:
                    print("------------------------------------------------------------- Enter email:")  

                    valid = False
                    while not valid:
                        selected = request_user_input_email(">>> Enter email adress: ")
                        if self.is_value_existing_in_db(selected, "email"): # check if the email is already in the db
                            print('email address already exists. Please try again')
                        else:
                            valid = True
                    
                    print("selected email address: ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["email"] = selected
                    else:
                        self.parent_view

                elif "phone" not in data:
                    print("------------------------------------------------------------- Enter phone:")

                    valid = False
                    while not valid:
                        selected = request_user_input_phone(">>> Enter phone number: ")
                        if self.is_value_existing_in_db(selected, "phone"): # check if the phone is already in the db                        
                            print('phone number already exists. Please try again')
                        else:
                            valid = True

                    print("selected phone no: ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["phone"] = selected
                    else:
                        self.parent_view

                else:
                    __confirmation = request_user_input_in_list(">>> Confirm pilot creation ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        creation_status = self.pilotTable.create_pilot(data)
                        print(creation_status)
                        __ = input("(press Enter)") 
                    else:
                        print("cancelled creation")
                        __ = input("(press Enter)")
                    complete = True

            self.view_menu()

        except Exception as e: # if exception, print + redirect to menu page
            print("Error : " + str(e))           
            self.view_menu() 

    # ###############################################################################################################################
    def is_value_existing_in_db(self, value_to_check, col_name):

        try:
            # get data from select query:
            data = self.pilotTable.select_all_values_from_col(col_name)  # list of the phone no of all pilots in the db
            if value_to_check in data:
                return True
            else:
                return False

        except Exception as e: # if exception, print + redirect to menu page
            print("Error : " + str(e))           
            self.view_menu() 

    ###############################################################################################################################
    def view_stats(self):
        '''
        display stats for pilots
        '''

        try:
            # # get data from select query:
            data = self.pilotTable.select_flight_stats_ytd()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n*************************************************************")
            print("*************************************************************  PILOT STATISTICS")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<26}{:<26}{:<26}{:<26}"
            print(formatspecifier.format("id",
                                        "first name",
                                        "last name", 
                                        "flight time YTD", 
                                        "number of flights YTD"
                                        ))
            print("-" * 110)

            for row in data:

                if row["nb_flights"] is not None:
                    row["hours"] = str(row["hours"])
                    if row["mins"] < 10:
                        row["mins"] = "0" + str(row["mins"])
                    else:
                        row["mins"] = str(row["mins"])

                    print(formatspecifier.format(str(row["id"]), 
                                                row["first_name"],                                                     
                                                row["last_name"], 
                                                row["hours"] + ":" + row["mins"], 
                                                row["nb_flights"]
                                                ))
                else:
                    print(formatspecifier.format(str(row["id"]), 
                                                row["first_name"],                                                     
                                                row["last_name"], 
                                                'None', 
                                                'None'
                                                ))                    

            print("-" * 110)

            __ = input("(press Enter)") 
            self.view_menu() 

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            self.view_menu() 



