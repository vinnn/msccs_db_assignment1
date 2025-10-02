import sqlite3

from pages.flightPage import FlightPage



while True:
  print("\n******************************************************************************")
  print("\t-------------")  
  print("\tGENERAL MENU:")
  print("\t-------------")
  print("\t 1. Flights")
  print("\t 2. Airports")
  print("\t 3. Pilots")
  print("\t-------------")
  print("\t 0. Exit")
  print("\t-------------")

  flightPage = FlightPage()

  __choose_menu = int(input("\t>>> Enter selection: "))
  if __choose_menu == 0:
    exit(0)
  if __choose_menu == 1:
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
    print("Invalid Choice")
