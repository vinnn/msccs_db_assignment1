
from dbtables.airportTable import AirportTable
from utils import request_user_input_int, request_user_input_in_list


class AirportPage:

    def __init__(self):
        self.airportTable = AirportTable()



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
                print(selected_airport)
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
                print(selected_airport)
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
                print(selected_airport)
                return selected_airport
                # self.viewDetailsOneFlight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            return None
