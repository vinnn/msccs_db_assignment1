
from dbtables.airportTable import AirportTable


airportTable = AirportTable()

from utils import request_user_input_int, request_user_input_in_list




class AirportPage:


    # def viewMenu(self):

    #     indent = " " * 5

    #     print("\n******************************************************************************")
    #     print(indent + "----------------------")        
    #     print(indent + "SCHEDULED FLIGHTS :")
    #     print(indent + "----------------------")
    #     print(indent + "1. All scheduled flights")
    #     print(indent + "2. 48HRS flight status")
    #     print(indent + "3. Flights by date")
    #     print(indent + "4. Flights by departure airport")
    #     print(indent + "5. Flights by arrival airport")   
    #     print(indent + "6. Flights by pilot assignment status")
    #     print(indent + "----------------------")  
    #     print(indent + "PAST FLIGHTS :")       
    #     print(indent + "----------------------")
    #     print(indent + "7. All past flights")  
    #     print(indent + "8. Statistics")
    #     print(indent + "----------------------")
    #     print(indent + "0. to go back")  
    #     print(indent + "M. to main menu")

    #     __user_input = request_user_input_in_list(">>> Enter selection: ", indent, ["0","1","2","3","4","5","6","7","8", "M"])

    #     if __user_input == "M":
    #         return
    #     elif __user_input == "0":
    #         return        
    #     elif __user_input == "1":
    #         self.viewAllFutureFlights()
    #     elif __user_input == "2":
    #         return
    #     elif __user_input == "3":
    #         return
    #     elif __user_input == "4":
    #         return
    #     elif __user_input == "5": 
    #         return
    #     elif __user_input == "6": 
    #         return
    #     elif __user_input == "7": 
    #         return
    #     elif __user_input == "8": 
    #         return
    #     else:
    #         print(indent + "Invalid Choice")   


    ###############################################################################################################################
    # def viewAllAirports(self, indent):
    #     '''
    #     display all airports
    #     '''

    #     indent = " " * 8

    #     try:
    #         # get data from select query:
    #         data = airportTable.select_all_airports()

    #         # display extracted data as a table:
    #         # print(indent + "----------------------")        
    #         # print(indent + "ALL AIRPORTS :")
    #         # print(indent + "----------------------")   
    #         formatspecifier = "{:<8}{:<6}{:<20}{:<20}{:<20}"
    #         print(formatspecifier.format(indent, "id", "name", "city", "country"))
    #         print(indent + "-" * 150)

    #         for row in data:
    #             print(formatspecifier.format(indent, row["id"], 
    #                                         row["name"][:18], 
    #                                         row["city"][:18], 
    #                                         row["country"][:18]
    #                                         ))
    #         print(indent + "-" * 150)

    #         # get list of flight id options from the table (add "0" for 'go back' option):
    #         list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
    #         # prompt the user to select an option: 
    #         __user_input = request_user_input_in_list(">>> For details and changes, select airport id (0 to go back): ", indent, list_ids_str)
            
    #         # redirect as per user selection:
    #         if __user_input =="0" :
    #             return
    #             # self.viewMenu() 
    #         else:
    #             return
    #             # self.viewDetailsOneFlight(int(__user_input))

    #     except Exception as e: # if exception, print + redirect to flight menu page
    #         print(indent + "Error : " + str(e))           
    #         # self.viewMenu() 


    ###############################################################################################################################
    def viewAirportSelection(self, indent):
        '''
        display all airport options
        '''

        indent = " " * 8

        try:
            # get data from select query:
            data = airportTable.select_all_airports()

            # display extracted data as a table:
            # print(indent + "----------------------")        
            # print(indent + "ALL AIRPORTS :")
            # print(indent + "----------------------")   
            formatspecifier = "{:<8}{:<6}{:<20}{:<20}{:<20}"
            print(formatspecifier.format(indent, "id", "name", "city", "country"))
            print(indent + "-" * 150)

            for row in data:
                print(formatspecifier.format(indent, row["id"], 
                                            row["name"][:18], 
                                            row["city"][:18], 
                                            row["country"][:18]
                                            ))
            print(indent + "-" * 150)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> Select airport id (0 to go back): ", indent, list_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                return
                # self.viewMenu() 
            else:
                selected_airport = [a for a in data if a["id"]==int(__user_input)][0]
                return selected_airport
                # self.viewDetailsOneFlight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print(indent + "Error : " + str(e))           
            # self.viewMenu() 



