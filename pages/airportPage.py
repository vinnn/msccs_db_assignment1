import os
from dbtables.airportTable import AirportTable
from utils import request_user_input_in_list, request_user_input_name


class AirportPage:

    ###############################################################################################################################
    def __init__(self):
        self.airportTable = AirportTable()
        self.parentView = self.view_menu

    ###############################################################################################################################
    def view_menu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n*************************************************************")
        print("************************************************************* AIRPORT MENU")   
        print("*************************************************************")
        print("1. All airports")
        print("2. Create new airport")
        print("----------------------")
        print("0. to go back")  
        print("----------------------")

        __user_input = request_user_input_in_list(">>> Enter selection: ", ["0","1","2","M"])

        if __user_input == "0":
            return
    
        elif __user_input == "1":
            self.view_all_airports()

        elif __user_input == "2":
            self.view_create_airport()
 
        else:
            print("Invalid Choice")  

    ###############################################################################################################################
    def view_all_airports(self):
        '''
        display information for all airports
        + prompt user to select one airport for details or make changes
        '''
        self.parentView = self.view_all_airports # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.airportTable.select_all_airports()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')  # clear screen before displaying page
            print("\n*************************************************************")
            print("************************************************************* ALL AIRPORTS")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<50}{:<26}{:<26}"
            print(formatspecifier.format("id",
                                        "name",
                                        "city", 
                                        "country"
                                        ))
            print("-" * 110)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["name"],                                                     
                                            row["city"], 
                                            row["country"]
                                            ))
            print("-" * 110)

            # get list of pilot id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select airport id (0 to go back): ", list_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.view_details_one_airport(int(__user_input))

        except Exception as e: # if exception, print + redirect to menu page
            print("Error : " + str(e))           
            self.view_menu() 

    ###############################################################################################################################
    def view_all_airport_selection(self): 
        '''
        display all airport options
        + prompt user to select an airport id
        '''

        try:
            # get data from select query:
            data = self.airportTable.select_all_airports()

            # display extracted data as a table:
            # print("----------------------")        
            # print("ALL AIRPORTS :")
            # print("----------------------")   
            formatspecifier = "{:<6}{:<20}{:<20}{:<20}"
            print(formatspecifier.format("id", "name", "city", "country"))
            print("-" * 60)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["name"][:18], 
                                            row["city"][:18], 
                                            row["country"][:18]
                                            ))
            print("-" * 60)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> Select airport id (0 to go back): ", list_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                return None
            else:
                selected_airport = [a for a in data if a["id"]==int(__user_input)][0]
                # print(selected_airport)
                return selected_airport
                # self.viewDetailsOneFlight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            return None
        
    ###############################################################################################################################
    def view_departure_airport_selection(self): 
        '''
        display all departure airport options
        + prompt user to select an airport id
        '''

        try:
            # get data from select query:
            data = self.airportTable.select_all_departure_airports()

            # display extracted data as a table: 
            formatspecifier = "{:<6}{:<20}{:<20}{:<20}"
            print(formatspecifier.format("id", "name", "city", "country"))
            print("-" * 60)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["name"][:18], 
                                            row["city"][:18], 
                                            row["country"][:18]
                                            ))
            print("-" * 60)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> Select airport id (0 to go back): ", list_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                return None
            else:
                selected_airport = [a for a in data if a["id"]==int(__user_input)][0]
                # print(selected_airport)
                return selected_airport
                # self.viewDetailsOneFlight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            return None

    ###############################################################################################################################
    def view_arrival_airport_selection(self): 
        '''
        display all arrival airport options
        + prompt user to select an airport id
        '''

        try:
            # get data from select query:
            data = self.airportTable.select_all_arrival_airports()

            # display extracted data as a table:
            formatspecifier = "{:<6}{:<20}{:<20}{:<20}"
            print(formatspecifier.format("id", "name", "city", "country"))
            print("-" * 60)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["name"][:18], 
                                            row["city"][:18], 
                                            row["country"][:18]
                                            ))
            print("-" * 60)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> Select airport id (0 to go back): ", list_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                return None
            else:
                selected_airport = [a for a in data if a["id"]==int(__user_input)][0]
                # print(selected_airport)
                return selected_airport
                # self.viewDetailsOneFlight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            return None

    ###############################################################################################################################
    def view_details_one_airport(self, airport_id):
        '''
        display details for one airport
        + menu for editing/deleting the airport
        + prompt user for menu selection
        '''

        try:
            data = self.airportTable.select_one_airport(airport_id)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n*************************************************************")
            print("************************************************************* AIRPORT DETAILS")   
            print("*************************************************************")
            print("{:<24}{:<24}\n".format("airport id",data["id"]))
            print("{:<24}{:<24}".format("airport name", data["name"]))            
            print("{:<24}{:<24}".format("airport city", data["city"]))
            print("{:<24}{:<24}".format("airport country", data["country"]))

            print("------------------------------------------------------------- Make changes:")  
            print("1. Change airport name")
            print("2. Change city")
            print("3. Change country")
            print("4. Delete airport")            
            print("0. to go back")
            print("M. to main menu")
            print("----------------------")
            __user_input = request_user_input_in_list(">>> Enter selection: ", ["0","1","2","3","4","M"])

            if __user_input == "0":
                self.parentView() # go back to previous view

            elif __user_input == "M":
                self.view_menu() # go back to menu

            elif __user_input == "1":
                print(f"------------------------------------------------------------ Enter new airport name: ")
                selected = request_user_input_name(">>> Enter new name: ")

                print("replace with ", selected)
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.airportTable.update_airport(airport_id, "name", selected)
                    print(update_status)
                    __ = input("(press Enter to refresh)") 
                    self.view_details_one_airport(airport_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)") 
                    self.view_details_one_airport(airport_id)

            elif __user_input == "2":
                print(f"------------------------------------------------------------ Enter new city: ")
                selected = request_user_input_name(">>> Enter new city: ")

                print("replace with ", selected)
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.airportTable.update_airport(airport_id, "city", selected)
                    print(update_status)
                    __ = input("(press Enter to refresh)") 
                    self.view_details_one_airport(airport_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)") 
                    self.view_details_one_airport(airport_id)

            elif __user_input == "3":
                print(f"------------------------------------------------------------ Enter new country: ")
                selected = request_user_input_name(">>> Enter new country: ")

                print("replace with ", selected)
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.airportTable.update_airport(airport_id, "country", selected)
                    print(update_status)
                    __ = input("(press Enter to refresh)") 
                    self.view_details_one_airport(airport_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)") 
                    self.view_details_one_airport(airport_id)

            elif __user_input == "4":
                print(f"------------------------------------------------------------ Delete airport:")
                __confirmation = request_user_input_in_list(">>> Confirm deletion ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    deletion_status = self.airportTable.delete_airport(airport_id)
                    print(deletion_status)
                    __ = input("(press Enter)") 
                    self.parentView()  # go back to previous view
                else:
                    print("cancelled deletion")
                    __ = input("(press Enter)") 
                    self.view_details_one_airport(airport_id)  


        except Exception as e: # if exception, print + redirect to all flight menu page
            print("Error : " + str(e))   
            self.view_menu() 

    # ###############################################################################################################################
    def view_create_airport(self):
        '''
        display form for airport creation
        '''
        self.parent_view = self.view_menu # to go back to this view when user goes back from detail view

        try:
            data = {}

            complete = False
            while not complete:
                os.system('cls' if os.name == 'nt' else 'clear')

                print("\n*************************************************************")
                print("************************************************************* NEW AIPORT")   
                print("*************************************************************")

                print("{:<24}{:<24}".format("airport name", data["name"] if "name" in data else ""))
                print("{:<24}{:<24}".format("city", data["city"] if "city" in data else ""))
                print("{:<24}{:<24}\n".format("country", data["country"] if "country" in data else ""))

                if "name" not in data:
                    print("------------------------------------------------------------- Enter airport name:")  
                    selected = request_user_input_name(">>> Enter airport name: ")
                    print("selected airport name: ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["name"] = selected
                    else:
                        complete = True 
                        self.parent_view

                elif "city" not in data:
                    print("------------------------------------------------------------- Enter airport city:")  
                    selected = request_user_input_name(">>> Enter city name: ")
                    print("selected city name: ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["city"] = selected
                    else:
                        complete = True 
                        self.parent_view

                elif "country" not in data:
                    print("------------------------------------------------------------- Enter airport country:")  
                    selected = request_user_input_name(">>> Enter country name: ")
                    print("selected country name: ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["country"] = selected
                    else:
                        complete = True 
                        self.parent_view
                else:
                    __confirmation = request_user_input_in_list(">>> Confirm airport creation ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        creation_status = self.airportTable.create_airport(data)
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

