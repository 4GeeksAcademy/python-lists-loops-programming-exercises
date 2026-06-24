parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here

def get_parking_lot(parking_state):
    total_slots = 0
    available_slots = 0
    occupied_slots = 0

    for fila in parking_state:
        for slot in fila:
            if slot != 0:
                total_slots += 1
                if slot == 1:
                    occupied_slots += 1
                elif slot == 2:
                    available_slots += 1

    return {
        "total_slots": total_slots,
        "available_slots": available_slots,
        "occupied_slots": occupied_slots
    }


print(get_parking_lot(parking_state))