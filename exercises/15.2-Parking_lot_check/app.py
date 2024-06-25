parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(lista):
    state = {'total_slots': 0, 'available_slots': 0, 'occupied_slots': 0}

    total = 0
    not_parking = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == 1:
                state["occupied_slots"] += 1
                total += 1
            elif lista[i][j] == 2:
                state["available_slots"] += 1
                total += 1

    total = total - not_parking
    state["total_slots"] = total

    return state


print(get_parking_lot(parking_state))