parking_state = [
  [1,1,1,2],
  [0,0,0,0],
  [1,1,2,2]
]

# Your code here
def get_parking_lot(spots):
    state = {
        "total_slots":0,
        "available_slots":0,
        "occupied_slots":0
    }
    width = len(spots[0])
    height = len(spots)
    for a in range(height):
      for i in range(width):
          if spots[a][i] == 1:
              state["occupied_slots"] += 1
              state["total_slots"] += 1
          elif spots[a][i] == 2:
              state["available_slots"] += 1
              state["total_slots"] += 1

    return state

print(get_parking_lot(parking_state))