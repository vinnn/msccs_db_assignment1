import os
from datetime import datetime, timedelta

from dbtables.flightTable import FlightTable
from pages.airportPage import AirportPage
from pages.pilotPage import PilotPage

from constants import PILOT_AVAILABILITY_MARGIN_DAYS
from utils import request_user_input_int, request_user_input_in_list, request_user_input_date, request_user_input_time


class FlightPage:

    def __init__(self):
        self.flightTable = FlightTable()
        self.airportPage = AirportPage()
        self.pilotPage = PilotPage()
        self.parent_view = self.view_menu
        self.page_selected_datetime = None # as an instance variable to enable easier navigation to parent views
        self.page_selected_airport_id = None

    ###############################################################################################################################
    def view_menu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n*************************************************************")
        print("************************************************************* FLIGHTS") 
        print("*************************************************************")
        print("----------------------")
        print("SCHEDULED FLIGHTS :")
        print("----------------------")
        print("1. Flight schedule")   # add pilot status
        print("2. Filter by departure date")   # add pilot status
        print("3. Filter by departure airport")   # add pilot status
        print("4. Filter by arrival airport")   # add pilot status
        print("5. Unassigned flights")
        print("6. Create new flight")
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
            self.view_all_scheduled_flights()

        elif __user_input == "2":
            # user selected departure date:
            selected_datetime = request_user_input_date(">>> Enter departure date (YYYY-MM-DD): ")
            if selected_datetime is not None:
                self.page_selected_datetime = selected_datetime #.strftime("%Y-%m-%d %H:%M:%S")
                self.view_flights_by_datetime()
            else: 
                self.view_menu()

        elif __user_input == "3":
            # show all departure airports + get user selected airport id:
            selected = self.airportPage.view_departure_airport_selection()
            if selected is not None:
                self.page_selected_airport_id = selected["id"]
                self.view_flights_by_departure_airport()
            else: # if user selected 0 to go back
                self.view_menu()

        elif __user_input == "4": 
            # show all arrival airports + get user selected airport id:
            selected = self.airportPage.view_arrival_airport_selection()
            if selected is not None:
                self.page_selected_airport_id = selected["id"]
                self.view_flights_by_arrival_airport()
            else: # if user selected 0 to go back
                self.view_menu()

        elif __user_input == "5": 
            self.view_all_unassigned_scheduled_flights()

        elif __user_input == "6": 
            self.view_create_flight()

        elif __user_input == "7": 
            self.view_past_flights()

        elif __user_input == "8": 
            return        
        else:
            print("Invalid Choice")   


    ###############################################################################################################################
    def view_all_scheduled_flights(self):
        '''
        display information for all future flights
        + prompt user to select one flight for details or make changes
        '''
        self.parent_view = self.view_all_scheduled_flights # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_all_future_flights()
            print(data)

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')  # clear screen before displaying page
            print("\n*************************************************************")
            print("************************************************************* ALL SCHEDULED FLIGHTS")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<14}{:<8}{:<26}{:<16}{:<16}{:<14}{:<8}{:<26}{:<16}{:<16}{:<12}{:<12}"
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
                                        "status",
                                        "pilot"
                                        ))
            print("-" * 185)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            datetime.strptime(row["departure_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["departure_time"],                                                     
                                            row["departure_airport"][:24], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12],
                                            datetime.strptime(row["arrival_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["arrival_time"],                                               
                                            row["arrival_airport"][:24],                                             
                                            row["arrival_city"][:12], 
                                            row["arrival_country"][:12], 
                                            row["status"],
                                            "assigned" if row["pilot"] is not None else "None",  
                                            ))
            print("-" * 185)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", list_flight_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.view_details_one_flight(int(__user_input))

        except Exception as e: # if exception, print + redirect to menu page
            print("Error : " + str(e))           
            self.view_menu() 


    ###############################################################################################################################
    def view_flights_by_datetime(self):
        '''
        display all flights departing on a certain date
        + prompt user to select one flight for details or make changes
        '''
        self.parent_view = self.view_flights_by_datetime # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_flights_by_departure_datetime(self.page_selected_datetime)

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n*************************************************************")
            print("************************************************************* FLIGHTS BY DEPARTURE DATE")   
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<14}{:<8}{:<26}{:<16}{:<16}{:<14}{:<8}{:<26}{:<16}{:<16}{:<12}{:<12}"
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
                                        "status",
                                        "pilot"
                                        ))
            print("-" * 185)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            datetime.strptime(row["departure_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["departure_time"],                                                     
                                            row["departure_airport"][:24], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12],
                                            datetime.strptime(row["arrival_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["arrival_time"],                                               
                                            row["arrival_airport"][:24],                                             
                                            row["arrival_city"][:12], 
                                            row["arrival_country"][:12], 
                                            row["status"],
                                            "assigned" if row["pilot"] is not None else "None",  
                                            ))
            print("-" * 185)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", list_flight_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.view_details_one_flight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            self.view_menu() 


    ###############################################################################################################################
    def view_flights_by_departure_airport(self):
        '''
        display all flights departing from a certain airport
        + prompt user to select one flight for details or make changes
        '''
        # self.parent_view = self.view_flights_by_departure_airport # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_flights_by_departure_airport(self.page_selected_airport_id)

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n*************************************************************")
            print("************************************************************* FLIGHTS BY DEPARTURE AIRPORT")   
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<14}{:<8}{:<26}{:<16}{:<16}{:<14}{:<8}{:<26}{:<16}{:<16}{:<12}{:<12}"
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
                                        "status",
                                        "pilot"
                                        ))
            print("-" * 185)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            datetime.strptime(row["departure_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["departure_time"],                                                     
                                            row["departure_airport"][:24], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12],
                                            datetime.strptime(row["arrival_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["arrival_time"],                                               
                                            row["arrival_airport"][:24],                                             
                                            row["arrival_city"][:12], 
                                            row["arrival_country"][:12], 
                                            row["status"],
                                            "assigned" if row["pilot"] is not None else "None",  
                                            ))
            print("-" * 185)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", list_flight_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.parent_view = self.view_flights_by_departure_airport # to go back to this view when user goes back from detail view
                self.view_details_one_flight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            self.view_menu() 


    ###############################################################################################################################
    def view_flights_by_arrival_airport(self):
        '''
        display all flights arriving to a certain airport
        + prompt user to select one flight for details or make changes
        '''
        # self.parent_view = self.view_flights_by_departure_airport # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_flights_by_arrival_airport(self.page_selected_airport_id)

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n*************************************************************")
            print("************************************************************* FLIGHTS BY ARRIVAL AIRPORT")   
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<14}{:<8}{:<26}{:<16}{:<16}{:<14}{:<8}{:<26}{:<16}{:<16}{:<12}{:<12}"
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
                                        "status",
                                        "pilot"
                                        ))
            print("-" * 185)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            datetime.strptime(row["departure_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["departure_time"],                                                     
                                            row["departure_airport"][:24], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12],
                                            datetime.strptime(row["arrival_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["arrival_time"],                                               
                                            row["arrival_airport"][:24],                                             
                                            row["arrival_city"][:12], 
                                            row["arrival_country"][:12], 
                                            row["status"],
                                            "assigned" if row["pilot"] is not None else "None",  
                                            ))
            print("-" * 185)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", list_flight_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.parent_view = self.view_flights_by_arrival_airport # to go back to this view when user goes back from detail view
                self.view_details_one_flight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            self.view_menu() 


    ###############################################################################################################################
    def view_all_unassigned_scheduled_flights(self):
        '''
        display information for all future flights for which no pilots have been assigned yet
        + prompt user to select one flight for details or make changes
        '''
        self.parent_view = self.view_all_unassigned_scheduled_flights # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_all_future_unassigned_flights()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')  # clear screen before displaying page
            print("\n*************************************************************")
            print("************************************************************* ALL SCHEDULED FLIGHTS")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<14}{:<8}{:<26}{:<16}{:<16}{:<14}{:<8}{:<26}{:<16}{:<16}{:<12}{:<12}"
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
                                        "status",
                                        "pilot"
                                        ))
            print("-" * 185)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            datetime.strptime(row["departure_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["departure_time"],                                                     
                                            row["departure_airport"][:24], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12],
                                            datetime.strptime(row["arrival_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["arrival_time"],                                               
                                            row["arrival_airport"][:24],                                             
                                            row["arrival_city"][:12], 
                                            row["arrival_country"][:12], 
                                            row["status"],
                                            row["pilot"] if row["pilot"] is not None else "None",                                            
                                            ))
            print("-" * 185)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", list_flight_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.view_details_one_flight(int(__user_input))

        except Exception as e: # if exception, print + redirect to menu page
            print("Error : " + str(e))           
            self.view_menu() 


    ###############################################################################################################################
    def view_past_flights(self):
        '''
        display information for all past flights
        '''
        # self.parent_view = self.view_past_flights # to go back to this view when user goes back from detail view

        try:
            # get data from select query:
            data = self.flightTable.select_all_past_flights()

            # display extracted data as a table:
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("\n*************************************************************")
            print("************************************************************* PAST FLIGHTS")  
            print("*************************************************************\n")

            formatspecifier = "{:<6}{:<14}{:<8}{:<26}{:<16}{:<16}{:<14}{:<8}{:<26}{:<16}{:<16}{:<12}{:<12}"
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
                                        "status",
                                        "pilot"
                                        ))
            print("-" * 185)

            for row in data:
                print(formatspecifier.format(row["id"], 
                                            datetime.strptime(row["departure_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["departure_time"],                                                     
                                            row["departure_airport"][:24], 
                                            row["departure_city"][:12], 
                                            row["departure_country"][:12],
                                            datetime.strptime(row["arrival_date"], "%Y-%m-%d").strftime("%d-%b-%Y"),
                                            row["arrival_time"],                                               
                                            row["arrival_airport"][:24],                                             
                                            row["arrival_city"][:12], 
                                            row["arrival_country"][:12], 
                                            row["status"],
                                            "assigned" if row["pilot"] is not None else "None",  
                                            ))
            print("-" * 185)

            # get list of flight id options from the table (add "0" for 'go back' option):
            list_flight_ids_str = [str(r["id"]) for r in data] + ["0"]
            
            # prompt the user to select an option: 
            __user_input = request_user_input_in_list(">>> For details and changes, select flight id (0 to go back): ", list_flight_ids_str)

            # redirect as per user selection:
            if __user_input =="0" :
                self.view_menu() 
            else:
                self.view_details_one_flight(int(__user_input))

        except Exception as e: # if exception, print + redirect to flight menu page
            print("Error : " + str(e))           
            self.view_menu() 


    ###############################################################################################################################
    def view_details_one_flight(self, flight_id):
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
            print("{:<24}{:<24}\n".format("flight id",data["id"]))
            print("{:<24}{:<24}".format("departure airport", data["departure_airport"] + ", " + data["departure_city"] + ", " + data["departure_country"]))            
            print("{:<24}{:<24}".format("departure date", data["departure_date"]))
            print("{:<24}{:<24}\n".format("departure time", data["departure_time"]))

            print("{:<24}{:<24}".format("arrival airport", data["arrival_airport"] + ", " + data["arrival_city"] + ", " + data["arrival_country"]))
            print("{:<24}{:<24}".format("arrival date", data["arrival_date"]))
            print("{:<24}{:<24}\n".format("arrival time", data["arrival_time"]))

            print("{:<24}{:<24}\n".format("flight duration", data["duration"]))

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
            print("4. Change arrival airport")
            print("5. Change duration")
            print("6. Change status")
            print("7. Assign/Change pilot")
            print("8. Unassign current pilot")            
            print("9. Delete flight")            
            print("0. to go back")
            print("M. to main menu")
            print("----------------------")
            __user_input = request_user_input_in_list(">>> Enter selection: ", ["0","1","2","3","4","5","6","7","8","9","M"])

            if __user_input == "0":
                self.parent_view() # go back to previous view

            elif __user_input == "M":
                self.view_menu()

            elif __user_input == "1":
                print(f"------------------------------------------------------------ Enter new departure date: ")
                selected = request_user_input_date(">>> Enter new date (YYYY-MM-DD): ")

                print("replace with ", selected.strftime("%Y-%m-%d"))
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "departure_date", selected.strftime("%Y-%m-%d"))
                    print(update_status)
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)")                    
                    self.view_details_one_flight(flight_id)

            elif __user_input == "2":
                print(f"------------------------------------------------------------ Enter new departure time: ")
                selected = request_user_input_time(">>> Enter new time (HR:MM): ")

                print("replace with ", selected.strftime("%H:%M"))
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "departure_time", selected.strftime("%H:%M"))
                    print(update_status)
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)")                    
                    self.view_details_one_flight(flight_id)

            elif __user_input == "3" or __user_input == "4":
                print(f"------------------------------------------------------------ Select new {'departure' if __user_input=='3' else 'arrival'} airport:")

                selected = self.airportPage.view_all_airport_selection()
                print("replace with ", selected["name"] + ", " + selected["city"] + ", " + selected["country"])
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "departure_airport_id" if __user_input=='3' else "arrival_airport_id", selected["id"])
                    print(update_status)
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)")                    
                    self.view_details_one_flight(flight_id)

            elif __user_input == "5":
                print(f"------------------------------------------------------------ Enter new duration: ")
                selected = request_user_input_time(">>> Enter new time (HR:MM): ")

                print("replace with ", selected.strftime("%H:%M"))
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "duration", selected.strftime("%H:%M"))
                    print(update_status)
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)")                    
                    self.view_details_one_flight(flight_id)


            elif __user_input == "6":
                print(f"------------------------------------------------------------ Enter new status: ")
                selected = request_user_input_in_list(">>> Enter new status (0: on time, 1: departed, 2: landed, 3: delayed, 4: cancelled): ", ["0","1","2","3","4"])

                print("replace with ", "on time" if selected == "0" else "departed" if selected == "1" else "landed" if selected == "2" else "delayed" if selected == "3" else "cancelled")
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "status_id", selected)
                    print(update_status)
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)")                    
                    self.view_details_one_flight(flight_id)

            elif __user_input == "7":
                print(f"------------------------------------------------------------ Select new pilot:")
                from_datetime = datetime.strptime(f"{data['departure_date']} {data['departure_time']}", "%Y-%m-%d %H:%M") - timedelta(days=PILOT_AVAILABILITY_MARGIN_DAYS)
                from_datetime_str = from_datetime.strftime("%Y-%m-%d %H:%M") 
                to_datetime = datetime.strptime(f"{data['arrival_date']} {data['arrival_time']}", "%Y-%m-%d %H:%M") + timedelta(days=PILOT_AVAILABILITY_MARGIN_DAYS)
                to_datetime_str = to_datetime.strftime("%Y-%m-%d %H:%M") 
                
                selected = self.pilotPage.view_available_pilots_by_period(from_datetime_str, to_datetime_str)

                print("replace with ", selected["first_name"] + ", " + selected["last_name"])
                __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    update_status = self.flightTable.update_flight(flight_id, "pilot_id", selected["id"])
                    print(update_status)
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)
                else:
                    print("cancelled update")
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)

            elif __user_input == "8":
                print(f"------------------------------------------------------------ Unassign current pilot:")

                if data["pilot_id"] is None:
                    print("invalid action (no pilot assigned)")
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)
                else:
                    print("unassign pilot : ", data["pilot_first_name"] + ", " + data["pilot_last_name"] + " (id=" + str(data["pilot_id"]) + ")")
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        update_status = self.flightTable.update_flight(flight_id, "pilot_id", None)
                        print(update_status)
                        __ = input("(press Enter)")
                        self.view_details_one_flight(flight_id)
                    else:
                        print("cancelled update")
                        __ = input("(press Enter)")                        
                        self.view_details_one_flight(flight_id)
            
            elif __user_input == "9":
                print(f"------------------------------------------------------------ Delete flight:")
                __confirmation = request_user_input_in_list(">>> Confirm deletion ? (Y/N): ", ["Y","N"])
                if __confirmation == "Y":
                    deletion_status = self.flightTable.delete_flight(flight_id)
                    print(deletion_status)
                    __ = input("(press Enter)")
                    self.parent_view()  # go back to previous view
                else:
                    print("cancelled deletion")
                    __ = input("(press Enter)")
                    self.view_details_one_flight(flight_id)            




        except Exception as e: # if exception, print + redirect to all flight menu page
            print("Error : " + str(e))   
            self.view_menu() 


    # ###############################################################################################################################
    def view_create_flight(self):
        '''
        display form for flight creation
        '''
        self.parent_view = self.view_menu 

        try:
            data = {}

            complete = False
            while not complete:
                os.system('cls' if os.name == 'nt' else 'clear')

                print("\n*************************************************************")
                print("************************************************************* NEW FLIGHT")   
                print("*************************************************************")
                departure_airport = data["departure_airport"] + ", " + data["departure_city"] + ", " + data["departure_country"] if "departure_airport_id" in data else ""
                print("{:<24}{:<24}".format("departure airport", departure_airport))
                print("{:<24}{:<24}".format("departure date", data["departure_date"] if "departure_date" in data else ""))
                print("{:<24}{:<24}\n".format("departure time", data["departure_time"] if "departure_time" in data else ""))

                arrival_airport = data["arrival_airport"] + ", " + data["arrival_city"] + ", " + data["arrival_country"] if "arrival_airport" in data else ""
                print("{:<24}{:<24}\n".format("arrival airport", arrival_airport))
                print("{:<24}{:<24}\n".format("flight duration", data["duration"] if "duration" in data else ""))
                print("{:<24}{:<24}".format("status", data["status"] if "status" in data else ""))

                pilot = data["pilot_first_name"] + ", " + data["pilot_last_name"] if "pilot_id" in data else ""
                print("{:<24}{:<24}\n\n".format("pilot", pilot))


                if "departure_airport_id" not in data:
                    print("------------------------------------------------------------- Enter departure airport:")  

                    selected = self.airportPage.view_all_airport_selection()
                    print("selected departure airport : ", selected["name"] + ", " + selected["city"] + ", " + selected["country"])
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["departure_airport_id"] = selected["id"]
                        data["departure_airport"] = selected["name"]
                        data["departure_city"] = selected["city"]
                        data["departure_country"] = selected["country"]
                    else:
                        self.parent_view

                elif "departure_date" not in data:
                    print("------------------------------------------------------------- Enter departure date:")  

                    selected = request_user_input_date(">>> Enter date (YYYY-MM-DD): ")
                    print("selected departure date ", selected)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["departure_date"] = selected.strftime("%Y-%m-%d")
                    else:
                        self.parent_view

                elif "departure_time" not in data:
                    print("------------------------------------------------------------- Enter departure time:")  

                    selected = request_user_input_time(">>> Enter new time (HR:MM): ")
                    print("selected departure time ", selected.strftime("%H:%M"))
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["departure_time"] = selected.strftime("%H:%M")
                        data["departure_datetime"] = datetime.strptime(f"{data['departure_date']} {data['departure_time']}", "%Y-%m-%d %H:%M")
                    else:
                        self.parent_view

                elif "arrival_airport_id" not in data:
                    print("------------------------------------------------------------- Enter arrival airport:")  

                    selected = self.airportPage.view_all_airport_selection()
                    print("selected arrival airport : ", selected["name"] + ", " + selected["city"] + ", " + selected["country"])
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["arrival_airport_id"] = selected["id"]
                        data["arrival_airport"] = selected["name"]
                        data["arrival_city"] = selected["city"]
                        data["arrival_country"] = selected["country"]
                    else:
                        self.parent_view

                elif "duration" not in data:
                    print("------------------------------------------------------------- Enter flight duration:")  

                    selected = request_user_input_time(">>> Enter duration (HR:MM): ")
                    print("selected flight duration : ", selected.strftime("%H:%M"))
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        arrival_datetime = data["departure_datetime"] + timedelta(hours=selected.hour, minutes=selected.minute)
                        data["arrival_datetime"] = arrival_datetime
                        data["arrival_date"] = arrival_datetime.strftime("%Y-%m-%d")
                        data["arrival_time"] = arrival_datetime.strftime("%H:%M")                        
                        data["duration"] = selected.strftime("%H:%M")
                    else:
                        self.parent_view

                elif "status_id" not in data:
                    print("------------------------------------------------------------- Enter flight status:")  

                    selected = request_user_input_in_list(">>> Enter new status (0: on time, 1: departed, 2: landed, 3: delayed, 4: cancelled): ", ["0","1","2","3","4"])
                    status = "on time" if selected == "0" else "departed" if selected == "1" else "landed" if selected == "2" else "delayed" if selected == "3" else "cancelled"
                    print("selected status : " + status)
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["status_id"] = selected
                        data["status"] = status
                    else:
                        self.parent_view

                elif "pilot_id" not in data:
                    print("------------------------------------------------------------- Enter pilot:")  

                    from_datetime = datetime.strptime(f"{data['departure_date']} {data['departure_time']}", "%Y-%m-%d %H:%M") - timedelta(days=PILOT_AVAILABILITY_MARGIN_DAYS)
                    from_datetime_str = from_datetime.strftime("%Y-%m-%d %H:%M") 
                    to_datetime = datetime.strptime(f"{data['arrival_date']} {data['arrival_time']}", "%Y-%m-%d %H:%M") + timedelta(days=PILOT_AVAILABILITY_MARGIN_DAYS)
                    to_datetime_str = to_datetime.strftime("%Y-%m-%d %H:%M") 
                    
                    selected = self.pilotPage.view_available_pilots_by_period(from_datetime_str, to_datetime_str)
                    print("selected pilot : ", selected["first_name"] + ", " + selected["last_name"])
                    __confirmation = request_user_input_in_list(">>> Confirm ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        data["pilot_id"] = selected["id"]
                        data["pilot_first_name"] = selected["first_name"]
                        data["pilot_last_name"] = selected["last_name"]
                    else:
                        self.parent_view

                else:
                    __confirmation = request_user_input_in_list(">>> Confirm flight creation ? (Y/N): ", ["Y","N"])
                    if __confirmation == "Y":
                        creation_status = self.flightTable.create_flight(data)
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


