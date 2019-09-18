parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

total = []
occupied = []
available = []
not_parking = []
parking_slots = {}
for numbs in parking_state:
    for digit in numbs:
        total.append(digit)
        if digit ==1:
            occupied.append(digit)
        elif digit == 2:
            available.append(digit)
        elif digit == 0:
            not_parking.append(digit)

parking_slots.update({"total": len(total), "occupied": len(occupied), "available": len(available), "not_parking": len(not_parking)})
print(parking_slots)

