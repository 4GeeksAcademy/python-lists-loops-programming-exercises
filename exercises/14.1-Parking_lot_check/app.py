parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

total = []
occupied = []
available = []
parking_slots = {}

def get_parking_lot(spaces):
    for numb in spaces:
        for digit in numb:
            total.append(digit)
            if digit == 1:
                occupied.append(digit)
            elif digit == 2:
                available.append(digit)
                parking_slots.update({'total': len(total), 'occupied': len(occupied), 'available': len(available)})
    return parking_slots
print(get_parking_lot(parking_state))

