
from dbtables.flightTable import FlightTable
from pages.airportPage import AirportPage

flightTable = FlightTable()

from utils import request_user_input_int, request_user_input_in_list




class FlightPage:


    def viewMenu(self):

        indent = " " * 5

        print("\n******************************************************************************")
        print(indent + "----------------------")        
        print(indent + "SCHEDULED FLIGHTS :")
        print(indent + "----------------------")
        print(indent + "1. All scheduled flights")
        print(indent + "2. 48HRS flight status")
        print(indent + "3. Flights by date")
        print(indent + "4. Flights by departure airport")
        print(indent + "5. Flights by arrival airport")   
        print(indent + "6. Flights by pilot assignment status")
        print(indent + "----------------------")  
        print(indent + "PAST FLIGHTS :")       
        print(indent + "----------------------")
        print(indent + "7. All past flights")  
        print(indent + "8. Statistics")
        print(indent + "----------------------")
        print(indent + "0. to go back")  
        print(indent + "M. to main menu")

        __user_input = request_user_input_in_list(">>> Enter selection: ", indent, ["0","1","2","3","4","5","6","7","8", "M"])

        if __user_input == "M":
            return
        elif __user_input == "0":
            return        
        elif __user_input == "1":
            self.viewAllFutureFlights()
        elif __user_input == "2":
            return
        elif __user_input == "3":
            return
        elif __user_input == "4":
            return
        elif __user_input == "5": 
            return
        elif __user_input == "6": 
            return
        elif __user_input == "7": 
            return
        elif __user_input == "8": 
            return
        else:
            print(indent + "Invalid Choice")   


    ###############################################################################################################################
    def viewAllFutureFlights(self):
        '''
        display all future flights
        + prompt user to select one flight for details or make changes
        '''

        indent = " " * 8

        try:
            # get data from select query:
            data = flightTable.select_all_future_flights()

            # display extracted data as a table:
            print(indent + "----------------------")        
            print(indent + "ALL FUTURE FLIGHTS :")
            print(indent + "----------------------")   
            formatspecifier = "{:<8}{:<6}{:<18}{:<14}{:<20}{:<16}{:<16}{:<20}{:<16}{:<16}{:<12}"
            print(formatspecifier.format(indent, "id",
                                        "departure date", 
                                        "time", 
                                        "from airport", 
                                        "city", 
                                        "country", 
                                        "to airport", 
                                        "city", 
                                        "country", 
                                        "status"
                                        ))
            print(indent + "-" * 150)

            for row in data:
                print(formatspecifier.format(indent, row["id"], 
                                            row["departure_date"][:10], 
                                            row["departure_time"][:10], 
                                            row["departure_airport"][:16], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12], 
                                            row["destination_airport"][:16], 
                                            row["destination_city"][:12], 
                                            row["destination_country"][:12], 
                                            row["status"]
                                            ))
            print(indent + "-" * 150)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", indent, list_flight_ids_str)
            
            # redirect as per user selection:
            if __user_input =="0" :
                self.viewMenu() 
            else:
                self.viewDetailsOneFlight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print(indent + "Error : " + str(e))           
            self.viewMenu() 



    ###############################################################################################################################
    def viewDetailsOneFlight(self, flight_id):
        '''
        display details of one flight
        + menu for editing/deleting the flight
        + prompt user for menu selection
        '''

        indent = " " * 12

        try:

            data = flightTable.select_one_flight(flight_id)

            print(indent + "-" * 80)  
            print(indent + "FLIGHT DETAILS :")
            print(indent + "-" * 80)            
            print("{:<12}{:<24}{:<24}".format(indent, "flight id",data["id"]))
            print("{:<12}{:<24}{:<24}".format(indent, "departure date", data["departure_date"]))
            print("{:<12}{:<24}{:<24}".format(indent, "departure time", data["departure_time"]))
            print("{:<12}{:<24}{:<24}".format(indent, "departure airport", data["departure_airport"] + ", " + data["departure_city"] + ", " + data["departure_country"]))
            print("{:<12}{:<24}{:<24}".format(indent, "destination airport", data["destination_airport"] + ", " + data["destination_city"] + ", " + data["destination_country"]))
            print("{:<12}{:<24}{:<24}".format(indent, "status", data["status"]))
            print("{:<12}{:<24}{:<24}".format(indent, "pilot", data["pilot_first_name"] + " " + data["pilot_last_name"]))  
            print(indent + "-" * 80)

            print(indent + "Make changes:")
            print(indent + "1. Change departure date")
            print(indent + "2. Change departure time")
            print(indent + "3. Change departure airport")
            print(indent + "4. Change destination airport")            
            print(indent + "5. Change status")
            print(indent + "6. Change pilot")
            print(indent + "7. Delete flight")            
            print(indent + "0. to go back")
            print(indent + "M. to main menu")

            __user_input = request_user_input_in_list(">>> Enter selection: ", indent, ["0","1","2","3","4","5","6","7","M"])

            if __user_input == "0":
                return
            elif __user_input == "M":
                return                    
            elif __user_input == "1":
                return
            elif __user_input == "2":
                return
            elif __user_input == "3":
                print(indent + "SELECT NEW DEPARTURE AIRPORT:")                
                airportPage = AirportPage()
                selected = airportPage.viewAirportSelection(indent)
                print("replace departure airport with ", selected["name"] + ", " + selected["city"] + ", " + selected["country"])
                __user_input = request_user_input_in_list(">>> Confirm ? (Y/N): ", indent, ["Y","N"])                
                # print("airportPage.selected_id", airportPage.selected_id)
                # flightTable.update_one_flight_airport(airportPage.selected_id, "departure_airport_id")
            elif __user_input == "4":
                return
            elif __user_input == "5": 
                return
            elif __user_input == "6": 
                return
            elif __user_input == "7": 
                return
            
        except Exception as e: # if exception, print + redirect to all flight menu page
            print(indent + "Error : " + str(e))   
            self.viewMenu() 


   