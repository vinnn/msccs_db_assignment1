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
  print(indent + "E. Exit")
  print(indent + "-------------")

  flightPage = FlightPage()

  __user_input = request_user_input_in_list(">>> Enter selection: ", indent, ["1","2","3","4","E"])

  if __user_input == "E":
    exit(0)
  if __user_input == "1":
    flightPage.viewMenu()
#   elif __user_input == 2:
#     flight_ops.select_all_flights()
#   elif __user_input == 3:
#     db_ops.select_all()
#   elif __user_input == 4:
#     pilot_ops.insert_new_pilot()  
  else:
    print(indent + "Invalid Choice")
