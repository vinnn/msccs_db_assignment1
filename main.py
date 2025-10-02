import sqlite3
import os

from pages.flightPage import FlightPage
from utils import request_user_input_in_list




while True:
  os.system('cls' if os.name == 'nt' else 'clear')  
  print("\n*************************************************************")
  print("************************************************************* GENERAL MENU")   
  print("*************************************************************")  
  print("1. Flights")
  print("2. Airports")
  print("3. Pilots")
  print("4. Edit/Delete")
  print("-------------")
  print("E. Exit")
  print("-------------")

  flightPage = FlightPage()

  __user_input = request_user_input_in_list(">>> Enter selection: ", ["1","2","3","4","E"])

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
    print("Invalid Choice")
