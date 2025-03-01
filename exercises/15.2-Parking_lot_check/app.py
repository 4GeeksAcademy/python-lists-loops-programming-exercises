parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(parking):
    state = {
     "total_slots": 0,
     "available_slots": 0,
     "occupied_slots": 0
    }
    for spaces in parking:
        for space in spaces:
            if space == 1:
                state["total_slots"] += 1
                state["occupied_slots"] += 1
            elif space == 2:
                state["total_slots"] += 1
                state["available_slots"] += 1
    return state            
print(get_parking_lot(parking_state))