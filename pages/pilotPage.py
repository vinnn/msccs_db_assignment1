
from dbtables.pilotTable import PilotTable
from utils import request_user_input_int, request_user_input_in_list


class PilotPage:

    def __init__(self):
        self.pilotTable = PilotTable()


    ###############################################################################################################################
    def viewPilotSelection(self):
        '''
        display all pilot options
        '''

        try:
            # get data from select query:
            data = self.pilotTable.select_all_pilots()

            formatspecifier = "{:<6}{:<20}{:<20}{:<30}{:<20}{:<20}"
            print(formatspecifier.format("id", "first_name", "last_name", "email", "phone", "current location"))
            print("-" * 120)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["first_name"][:18], 
                                            row["last_name"][:18], 
                                            row["email"],
                                            row["phone"][:18],
                                            row["current_location_city"] + ", " + row["current_location_country"]
                                            ))
            print("-" * 120)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> Select pilot id (0 to go back): ", list_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                return
                # self.viewMenu() 
            else:
                selected_row = [a for a in data if a["id"]==int(__user_input)][0]
                return selected_row

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            # self.viewMenu() 



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
                # self.viewMenu() 
            else:
                selected_row = [a for a in data if a["id"]==int(__user_input)][0]
                return selected_row

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            # self.viewMenu() 

