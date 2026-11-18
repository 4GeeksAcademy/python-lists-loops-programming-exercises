parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here

# parkinglot_dict = {
#         "total_slots":0,
#         "available_slots":0,
#         "occupied_slots":0
#     }

def get_parking_lot(parking_state):
    parkinglotStatus =  {
        "total_slots":0,
        "available_slots":0,
        "occupied_slots":0
    }
    for row in parking_state:
        for col in row:
            if col == 1:
                parkinglotStatus["occupied_slots"] += 1
            elif col == 2:
                parkinglotStatus["available_slots"] += 1
        parkinglotStatus["total_slots"] =  parkinglotStatus["occupied_slots"] + parkinglotStatus["available_slots"]          
    return parkinglotStatus

print(get_parking_lot(parking_state))

