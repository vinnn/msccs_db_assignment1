import os

from dbtables.flightTable import FlightTable
from pages.airportPage import AirportPage

flightTable = FlightTable()

from utils import request_user_input_int, request_user_input_in_list




class FlightPage:


    def viewMenu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n*************************************************************")
        print("************************************************************* FLIGHTS")   
        print("*************************************************************")
        print("----------------------")
        print("SCHEDULED FLIGHTS :")
        print("----------------------")
        print("1. All scheduled flights")
        print("2. 48HRS flight status")
        print("3. Flights by date")
        print("4. Flights by departure airport")
        print("5. Flights by arrival airport")   
        print("6. Flights by pilot assignment status")
        print("----------------------")  
        print("PAST FLIGHTS :")       
        print("----------------------")
        print("7. All past flights")  
        print("8. Statistics")
        print("----------------------")
        print("0. to go back")  
        print("M. to main menu")
        print("----------------------")

        __user_input = request_user_input_in_list(">>> Enter selection: ", ["0","1","2","3","4","5","6","7","8", "M"])

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
            print("Invalid Choice")   


    ###############################################################################################################################
    def viewAllFutureFlights(self):
        '''
        display all future flights
        + prompt user to select one flight for details or make changes
        '''

        try:
            # get data from select query:
            data = flightTable.select_all_future_flights()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n*************************************************************")
            print("************************************************************* ALL SCHEDULED FLIGHTS")   
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<18}{:<14}{:<20}{:<16}{:<16}{:<20}{:<16}{:<16}{:<12}"
            print(formatspecifier.format("id",
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
            print("-" * 150)

            for row in data:
                print(formatspecifier.format(row["id"], 
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
            print("-" * 150)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", list_flight_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.viewMenu() 
            else:
                self.viewDetailsOneFlight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            self.viewMenu() 



    ###############################################################################################################################
    def viewDetailsOneFlight(self, flight_id):
        '''
        display details of one flight
        + menu for editing/deleting the flight
        + prompt user for menu selection
        '''

        try:
            data = flightTable.select_one_flight(flight_id)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n*************************************************************")
            print("************************************************************* FLIGHT DETAILS")   
            print("*************************************************************")
            print("{:<24}{:<24}".format("flight id",data["id"]))
            print("{:<24}{:<24}".format("departure date", data["departure_date"]))
            print("{:<24}{:<24}".format("departure time", data["departure_time"]))
            print("{:<24}{:<24}".format("departure airport", data["departure_airport"] + ", " + data["departure_city"] + ", " + data["departure_country"]))
            print("{:<24}{:<24}".format("destination airport", data["destination_airport"] + ", " + data["destination_city"] + ", " + data["destination_country"]))
            print("{:<24}{:<24}".format("status", data["status"]))
            if data["pilot_id"] is None:
                print("{:<24}{:<24}".format("pilot", "None"))
            else:
                print("{:<24}{:<24}".format("pilot", data["pilot_first_name"] + " " + data["pilot_last_name"]))  
            print("------------------------------------------------------------- Make changes:")  

            # print("Make changes:")
            print("1. Change departure date")
            print("2. Change departure time")
            print("3. Change departure airport")
            print("4. Change destination airport")            
            print("5. Change status")
            print("6. Change pilot")
            print("7. Delete flight")            
            print("0. to go back")
            print("M. to main menu")
            print("----------------------")
            __user_input = request_user_input_in_list(">>> Enter selection: ", ["0","1","2","3","4","5","6","7","M"])

            if __user_input == "0":
                self.viewAllFutureFlights()                
            elif __user_input == "M":
                self.viewMenu()                  
            elif __user_input == "1":
                return
            elif __user_input == "2":
                return
            elif __user_input == "3":
                print("------------------------------------------------------------ Select new departure airport:")
                airportPage = AirportPage()
                selected = airportPage.viewAirportSelection()
                print("replace departure airport with ", selected["name"] + ", " + selected["city"] + ", " + selected["country"])
                __user_input = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __user_input == "Y":
                    update_status = flightTable.update_flight(flight_id, "departure_airport_id", selected["id"])
                    print(update_status)
                    self.viewAllFutureFlights()
                else:
                    print("cancelled update")
                    self.viewAllFutureFlights()

            elif __user_input == "4":
                return
            elif __user_input == "5":
                return
            elif __user_input == "6":
                return
            elif __user_input == "7":
                return
            
        except Exception as e: # if exception, print + redirect to all flight menu page
            print("Error : " + str(e))   
            self.viewMenu() 


   