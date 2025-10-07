import sqlite3
import os

from pages.flightPage import FlightPage
from pages.pilotPage import PilotPage
from pages.airportPage import AirportPage
from dbtables.statusTable import StatusTable
from utils import request_user_input_in_list


while True:
  os.system('cls' if os.name == 'nt' else 'clear')  
  print("\n*************************************************************")
  print("************************************************************* MAIN MENU")   
  print("*************************************************************")  
  print("1. Flights")
  print("2. Pilots")
  print("3. Airports")
  print("-------------")
  print("E. Exit")
  print("-------------")

  flightPage = FlightPage()
  pilotPage = PilotPage()
  airportPage = AirportPage()
  statusTable = StatusTable()

  __user_input = request_user_input_in_list(">>> Enter selection: ", ["1","2","3","E"])

  if __user_input == "E":
    exit(0)
  if __user_input == "1":
    flightPage.view_menu()
  elif __user_input == "2":
    pilotPage.view_menu()
  elif __user_input == "3":
    airportPage.view_menu()
#     db_ops.select_all()
#   elif __user_input == "4":
#     pilot_ops.insert_new_pilot()  
  else:
    print("Invalid Choice")



# ASSUMPTIONS:
# - flight duration max is 24HRS