
from dbtables.flightTable import FlightTable

flightTable = FlightTable()

from utils import request_user_input_int




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


        __choose_menu = request_user_input_int(">>> Enter selection (0 for exit): ", indent)

        if __choose_menu == 0:
            return
        elif __choose_menu == 1:
            self.viewAllFutureFlights()
        elif __choose_menu == 2:
            return
        elif __choose_menu == 3:
            return
        elif __choose_menu == 4:
            return
        elif __choose_menu == 5: 
            return
        elif __choose_menu == 6: 
            return
        elif __choose_menu == 7: 
            return
        elif __choose_menu == 8: 
            return
        else:
            print(indent + "Invalid Choice")   


    ###############################################################################################################################
    def viewAllFutureFlights(self):
        '''
        display all future flights
        + prompt user for flight selection
        '''

        indent = " " * 8

        data = flightTable.select_all_future_flights()

        print(indent + "----------------------")        
        print(indent + "ALL FUTURE FLIGHTS :")
        print(indent + "----------------------")   
        # headers = ["id","departure date", "time","from airport","city", "country","to airport","city","country","status"]
        formatspecifier = "{:<8}{:<6}{:<18}{:<14}{:<20}{:<16}{:<16}{:<20}{:<16}{:<16}{:<12}"
        # print(formatspecifier.format(*headers)) # *: unpack argument sequence

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

        __selected_flight_id = request_user_input_int("For details or changes, select flight id (0 for back): ", indent)

        if __selected_flight_id == 0:
            self.viewMenu() 
        elif __selected_flight_id > 0 :
            self.viewOneFlight(__selected_flight_id)
        else:
            print("Invalid Choice")


    ###############################################################################################################################
    def viewOneFlight(self, flight_id):
        '''
        display details of one flight
        + menu for editing/deleting the flight
        + prompt user for menu selection
        '''

        if flight_id == 0:
            return
        else:
            flightTable.select_one_flight(flight_id)

            print("\n Menu:")
            print("**********")
            print(" 1. Amend departure date")
            print(" 2. Amend departure time")
            print(" 3. Amend status")
            print(" 4. Amend pilot")
            print(" 0. Exit\n")

            __choose_menu = int(input("Enter your choice: "))
            if __choose_menu == 1:
                return
            elif __choose_menu == 2:
                return
            elif __choose_menu == 3:
                return
            elif __choose_menu == 4:
                return
            elif __choose_menu == 0: 
                return

    # def 
        # while True:
        #     print("\n Menu:")
        #     print("**********")
        #     print(" 1. Flights")
        #     print(" 2. Pilots")   # filter vs destination, status, departure date
        #     print(" 3. Airports")
        #     print(" 4. Routes")                                                           #DONE
        #     print(" 5. Exit\n")




