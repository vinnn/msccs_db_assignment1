import sqlite3

from pages.flightPage import FlightPage
from utils import request_user_input_in_list


indent = " " * 2

while True:
  print("\n******************************************************************************")
  print(indent + "-------------")  
  print(indent + "GENERAL MENU:")
  print(indent + "-------------")
  print(indent + "1. Flights")
  print(indent + "2. Airports")
  print(indent + "3. Pilots")
  print(indent + "4. Edit/Delete")
  print(indent + "-------------")
  print(indent + "0. Exit")
  print(indent + "-------------")

  flightPage = FlightPage()

  __choose_menu = request_user_input_in_list(">>> Enter selection: ", indent, [0,1,2,3,4])

  if __choose_menu == "0":
    exit(0)
  if __choose_menu == "1":
    flightPage.viewMenu()
#   elif __choose_menu == 2:
#     flight_ops.select_all_flights()
#   elif __choose_menu == 3:
#     db_ops.select_all()
#   elif __choose_menu == 4:
#     pilot_ops.insert_new_pilot()
#   elif __choose_menu == 5: 
#     pilot_ops.select_all_pilots()
#   elif __choose_menu == 6:
#     pilot_ops.insert_new_pilot()
#   elif __choose_menu == 7:
#     airport_ops.insert_new_airport()
#   elif __choose_menu == 8:
#     airport_ops.select_all_airports()
#   elif __choose_menu == 9:                # DONE
#     route_ops.insert_new_route()
#   elif __choose_menu == 10:               # DONE
#     route_ops.select_all_routes()
#   elif __choose_menu == 11:               # DONE
#     exit(0)    
  else:
    print(indent + "Invalid Choice")
