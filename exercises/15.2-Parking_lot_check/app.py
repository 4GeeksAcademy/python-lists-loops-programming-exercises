parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(matrix):
  state = {'total_slots': 0, 'available_slots': 0, 'occupied_slots': 0}
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 1:
        state["occupied_slots"] += 1
        state["total_slots"] += 1
      elif matrix[i][j] == 2:
        state["available_slots"] += 1
        state["total_slots"] += 1
  return state

get_parking_lot(parking_state)