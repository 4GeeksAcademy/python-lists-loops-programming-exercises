parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]


#Your code go here:

total_slots = []
available_slots = []
occupied_slots = []
not_parking_slots = []
new_dict = {}


for x in parking_state:
    for j in x:
        if j == 1:
            occupied_slots.append(j)

for numb in parking_state:
    for n in numb:
        if n ==2:
            available_slots.append(n)

for number in parking_state:
    for o in number:
        total_slots.append(o)

for h in parking_state:
    for k in h:
        if k == 0:
            not_parking_slots.append(k)

new_dict.update({"total_slots" : len(total_slots), "occupied_slots":len(occupied_slots), "available_slots": len(available_slots), "not_parking_slots": len(not_parking_slots)})
print(new_dict)

