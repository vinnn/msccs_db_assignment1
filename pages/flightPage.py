import os
from datetime import datetime


from dbtables.flightTable import FlightTable
from pages.airportPage import AirportPage
from pages.pilotPage import PilotPage



from utils import request_user_input_int, request_user_input_in_list, request_user_input_date, request_user_input_time




class FlightPage:

    def __init__(self):
        self.flightTable = FlightTable()
        self.airportPage = AirportPage()
        self.pilotPage = PilotPage()
        self.parentView = self.viewMenu
        self.view_flights_by_date_selected_date = None # as an instance variable to enable easier navigation to parent views
        self.view_flights_by_departure_airport_selected_airport_id = None

    def viewMenu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n*************************************************************")
        print("************************************************************* FLIGHTS")   
        print("*************************************************************")
        print("----------------------")
        print("SCHEDULED FLIGHTS :")
        print("----------------------")
        print("1. Public flight schedule")
        print("2. 48HRS flight status")
        print("3. Flights by date")
        print("4. Flights by departure airport")
        print("5. Flights by arrival airport")   
        print("6. Flights by pilot assignment status")
        print("7. Create new flight")        
        print("----------------------")  
        print("PAST FLIGHTS :")       
        print("----------------------")
        print("8. All past flights")  
        print("9. Statistics")
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
            self.view_public_flight_schedule()
        elif __user_input == "2":
            return
        elif __user_input == "3":
            # user selected departure date:
            selected_date = request_user_input_date(">>> Enter departure date (YYYY-MM-DD): ")
            self.view_flights_by_date_selected_date = selected_date.strftime("%Y-%m-%d")
            self.view_flights_by_date()

        elif __user_input == "4":
            selected = self.airportPage.viewAirportSelection()
            self.view_flights_by_departure_airport_selected_airport_id = selected["id"]
            self.view_flights_by_departure_airport()

        elif __user_input == "5": 
            return
        elif __user_input == "6": 
            return
        elif __user_input == "7": 
            return
        elif __user_input == "8": 
            self.view_past_flights()
        elif __user_input == "9": 
            return        
        else:
            print("Invalid Choice")   


    ###############################################################################################################################
    def view_public_flight_schedule(self):
        '''
        display public information for all future flights
        + prompt user to select one flight for details or make changes
        '''
        self.parentView = self.view_public_flight_schedule # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_all_future_flights()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n*************************************************************")
            print("************************************************************* PUBLIC FLIGHT SCHEDULE")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<14}{:<8}{:<26}{:<16}{:<16}{:<14}{:<8}{:<26}{:<16}{:<16}{:<12}"
            print(formatspecifier.format("id",
                                        "departure",
                                        "time", 
                                        "from airport", 
                                        "city", 
                                        "country", 
                                        "arrival",
                                        "time",
                                        "at airport", 
                                        "city", 
                                        "country", 
                                        "status"
                                        ))
            print("-" * 175)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            datetime.strptime(row["departure_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            datetime.strptime(row["departure_time"], "%H:%M:%S").strftime("%H:%M"),  
                                            row["departure_airport"][:24], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12],
                                            datetime.strptime(row["arrival_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),          
                                            datetime.strptime(row["arrival_time"], "%H:%M:%S").strftime("%H:%M"),
                                            row["arrival_airport"][:24],                                             
                                            row["arrival_city"][:12], 
                                            row["arrival_country"][:12], 
                                            row["status"]
                                            ))
            print("-" * 175)

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
    def view_flights_by_date(self):
        '''
        display all flights departing on a certain date
        + prompt user to select one flight for details or make changes
        '''
        self.parentView = self.view_flights_by_date # to go back to this view when user goes back from detail view

        try:


            # get data from select query:
            data = self.flightTable.select_flights_by_departure_date(self.view_flights_by_date_selected_date)

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n*************************************************************")
            print("************************************************************* FLIGHTS BY DATE")   
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
    def view_flights_by_departure_airport(self):
        '''
        display all flights departing from a certain airport
        + prompt user to select one flight for details or make changes
        '''
        self.parentView = self.view_flights_by_departure_airport # to go back to this view when user goes back from detail view

        try:


            # get data from select query:
            data = self.flightTable.select_flights_by_departure_airport(self.view_flights_by_departure_airport_selected_airport_id)

            print(data)

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n*************************************************************")
            print("************************************************************* FLIGHTS BY DEPARTURE AIRPORT")   
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
    def view_past_flights(self):
        '''
        display information for all past flights
        '''
        # self.parentView = self.view_past_flights # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_all_past_flights()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n*************************************************************")
            print("************************************************************* PAST FLIGHTS")  
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
            data = self.flightTable.select_one_flight(flight_id)
            
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
                # self.view_public_flight_schedule()
                self.parentView() # go back to previous view

            elif __user_input == "M":
                self.viewMenu()

            elif __user_input == "1":
                print(f"------------------------------------------------------------ Enter new departure date: ")
                selected = request_user_input_date(">>> Enter new date (YYYY-MM-DD): ")

                print("replace with ", selected.strftime("%Y-%m-%d"))
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "departure_date", selected.strftime("%Y-%m-%d"))
                    print(update_status)
                    self.viewDetailsOneFlight(flight_id)
                else:
                    print("cancelled update")
                    self.viewDetailsOneFlight(flight_id)

            elif __user_input == "2":
                print(f"------------------------------------------------------------ Enter new departure time: ")
                selected = request_user_input_time(">>> Enter new time (HR:MM): ")

                print("replace with ", selected.strftime("%H:%M"))
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "departure_time", selected.strftime("%H:%M"))
                    print(update_status)
                    self.viewDetailsOneFlight(flight_id)
                else:
                    print("cancelled update")
                    self.viewDetailsOneFlight(flight_id)

            elif __user_input == "3" or __user_input == "4":
                print(f"------------------------------------------------------------ Select new {'departure' if __user_input=='3' else 'destination'} airport:")

                selected = self.airportPage.viewAirportSelection()
                print("replace with ", selected["name"] + ", " + selected["city"] + ", " + selected["country"])
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "departure_airport_id" if __user_input=='3' else "destination_airport_id", selected["id"])
                    print(update_status)
                    self.viewDetailsOneFlight(flight_id)
                else:
                    print("cancelled update")
                    self.viewDetailsOneFlight(flight_id)

            elif __user_input == "5":
                print(f"------------------------------------------------------------ Enter new status: ")
                selected = request_user_input_in_list(">>> Enter new status (0: on time, 1: departed, 2: landed, 3: delayed, 4: cancelled): ", ["0","1","2","3","4"])

                print("replace with ", "on time" if selected == "0" else "departed" if selected == "1" else "landed" if selected == "2" else "delayed" if selected == "3" else "cancelled")
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "status_id", selected)
                    print(update_status)
                    self.viewDetailsOneFlight(flight_id)
                else:
                    print("cancelled update")
                    self.viewDetailsOneFlight(flight_id)

            elif __user_input == "6":
                print(f"------------------------------------------------------------ Select new pilot:")
                selected = self.pilotPage.viewPilotSelection()

                print("replace with ", selected["first_name"] + ", " + selected["last_name"])
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "pilot_id", selected["id"])
                    print(update_status)
                    self.viewDetailsOneFlight(flight_id)
                else:
                    print("cancelled update")
                    self.viewDetailsOneFlight(flight_id)
            
            elif __user_input == "7":
                print(f"------------------------------------------------------------ Delete flight:")
                __confirmation = request_user_input_in_list(">>> Confirm deletion ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    deletion_status = self.flightTable.delete_flight(flight_id)
                    print(deletion_status)
                    # self.view_public_flight_schedule()
                    self.parentView()  # go back to previous view
                else:
                    print("cancelled deletion")
                    self.viewDetailsOneFlight(flight_id)            




        except Exception as e: # if exception, print + redirect to all flight menu page
            print("Error : " + str(e))   
            self.viewMenu() 


   