
from dbtables.pilotTable import PilotTable


pilotTable = PilotTable()

from utils import request_user_input_int, request_user_input_in_list


class PilotPage:
    ###############################################################################################################################
    def viewPilotSelection(self):
        '''
        display all pilot options
        '''

        try:
            # get data from select query:
            data = pilotTable.select_all_pilots()

            formatspecifier = "{:<6}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}"
            print(formatspecifier.format("id", "first_name", "last_name", "email", "phone", "current_location_city", "current_location_country"))
            print("-" * 60)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            row["first_name"][:18], 
                                            row["last_name"][:18], 
                                            row["email"][:18],
                                            row["phone"][:18],
                                            row["current_location_city"][:18],
                                            row["current_location_country"][:18]
                                            ))
            print("-" * 60)

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



