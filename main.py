import sqlite3
import os

from pages.flightPage import FlightPage
from pages.pilotPage import PilotPage
from utils import request_user_input_in_list




while True:
  os.system('cls' if os.name == 'nt' else 'clear')  
  print("\n*************************************************************")
  print("************************************************************* GENERAL MENU")   
  print("*************************************************************")  
  print("1. Flights")
  print("2. Pilots")
  print("3. Airports")
  print("-------------")
  print("E. Exit")
  print("-------------")

  flightPage = FlightPage()
  pilotPage = PilotPage()

  __user_input = request_user_input_in_list(">>> Enter selection: ", ["1","2","3","E"])

  if __user_input == "E":
    exit(0)
  if __user_input == "1":
    flightPage.view_menu()
  elif __user_input == "2":
    pilotPage.view_menu()
#     flight_ops.select_all_flights()
#   elif __user_input == "3":
#     db_ops.select_all()
#   elif __user_input == "4":
#     pilot_ops.insert_new_pilot()  
  else:
    print("Invalid Choice")
