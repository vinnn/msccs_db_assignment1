import sqlite3
import os

from pages.flightPage import FlightPage
from pages.pilotPage import PilotPage
from pages.airportPage import AirportPage
from dbtables.statusTable import StatusTable
from utils import request_user_input_in_list

while True:
  # clear the terminal screen before displaying the program menu:
  os.system('cls' if os.name == 'nt' else 'clear')

  # render the main menu:
  print("\n*************************************************************")
  print("************************************************************* MAIN MENU")   
  print("*************************************************************")  
  print("1. Flights")
  print("2. Pilots")
  print("3. Airports")
  print("-------------")
  print("E. Exit")
  print("-------------")

  # Instantiate objects handling the flight, pilot, airport and status views and data:
  flightPage = FlightPage()
  pilotPage = PilotPage()
  airportPage = AirportPage()
  statusTable = StatusTable()

  # prompt user for menu option selection:
  __user_input = request_user_input_in_list(">>> Enter selection: ", ["1","2","3","E"])

  if __user_input == "E":
    exit(0)
  if __user_input == "1":
    flightPage.view_menu()
  elif __user_input == "2":
    pilotPage.view_menu()
  elif __user_input == "3":
    airportPage.view_menu() 
  else:
    print("Invalid Choice")
