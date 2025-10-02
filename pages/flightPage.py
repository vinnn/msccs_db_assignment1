
from dbtables.flightTable import FlightTable

flightTable = FlightTable()

from utils import request_user_input_int




class FlightPage:


    def viewMenu(self):

        print("\n******************************************************************************")
        print("\t----------------------")        
        print("\tSCHEDULED FLIGHTS :")
        print("\t----------------------")
        print("\t 1. All flights")
        print("\t 2. 48HRS schedule")
        print("\t 3. Flights by date")
        print("\t 4. Flights by departure airport")
        print("\t 5. Flights by arrival airport")   
        print("\t 6. Flights by pilot assignment status")
        print("\t----------------------")  
        print("\tPAST FLIGHTS :")       
        print("\t----------------------")
        print("\t 7. All flights")  
        print("\t 8. Statistics")
        print("\t----------------------")


        __choose_menu = request_user_input_int("\t >>> Enter selection (0 for exit): ")

        if __choose_menu == 0:
            return
        elif __choose_menu == 1:
            self.viewAllFlights()
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



    def viewAllFlights(self):

        flightTable.select_all_flights()

        # selected_flightId = int(input("Select flight id (0 for exit): "))

        selected_flightId = request_user_input_int("\tFor details or changes, select flight id (0 for exit): ")


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




