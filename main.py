import sqlite3

from dboperations import DBOperations
from dbtables.pilotTable import PilotTable
from dbtables.airportTable import AirportTable
from dbtables.routeTable import RouteTable
from dbtables.flightTable import FlightTable


# - view all flights
# - view flight by multiple criteria 
#     - destination
#     - status
#     - departure date
# - update flight info
# - assign pilot to flight
# - view pilot schedule
# - view destination information
#     - update 

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Add a new flight")
  print(" 2. View flights")   # filter vs destination, status, departure date
  print(" 3. Update flight")
  print(" 4. Add a new pilot") 
  print(" 5. View pilots")     # filter with availability / select pilot / see schedule
  print(" 6. Assign pilot to flight")
  print(" 7. Add a new destination (airport)")
  print(" 8. View destination (airport) information")   # / update
  print(" 9. Add a new flight route")                                                         #DONE
  print(" 10. View flight routes")                                                            #DONE
  print(" 11. Exit\n")





  db_ops = DBOperations()
  pilot_ops = PilotTable()
  airport_ops = AirportTable()
  route_ops = RouteTable()
  flight_ops = FlightTable()

  __choose_menu = int(input("Enter your choice: "))
  # db_ops = DBOperations()    # this is the original location
  if __choose_menu == 1:
    flight_ops.insert_new_flight()
    # db_ops.create_table()
  elif __choose_menu == 2:
    flight_ops.select_all_flights()
  elif __choose_menu == 3:
    db_ops.select_all()
  elif __choose_menu == 4:
    pilot_ops.insert_new_pilot()
  elif __choose_menu == 5: 
    pilot_ops.select_all_pilots()
  elif __choose_menu == 6:
    pilot_ops.insert_new_pilot()
  elif __choose_menu == 7:
    airport_ops.insert_new_airport()
  elif __choose_menu == 8:
    airport_ops.select_all_airports()
  elif __choose_menu == 9:                # DONE
    route_ops.insert_new_route()
  elif __choose_menu == 10:               # DONE
    route_ops.select_all_routes()
  elif __choose_menu == 11:               # DONE
    exit(0)    
  else:
    print("Invalid Choice")
