
from dbtables.flightTable import FlightTable

flightTable = FlightTable()

from utils import request_user_input_int

class FlightPage:

    def generalView(self):
        flightTable.select_all_flights()

        # selected_flightId = int(input("Select flight id (0 for exit): "))

        selected_flightId = request_user_input_int("Select flight id (0 for exit): ")


        self.detailView(selected_flightId)


    def detailView(self, flightId):

        if flightId == 0:
            return
        else:
            flightTable.select_one_flight(flightId)

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




