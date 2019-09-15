# `14.1` Parking Lot

We can use a 2 dimensional array (matrix) to represent the current state of a parking lot like this:
![Parking lot](https://storage.googleapis.com/replit/images/1558366147943_71c41e2a3f01564b5bdba6618797af79.pn)
```py
parking_state = [
  [1,0,1,1,0,1],
  [2,0,1,1,0,1],
  [1,0,2,1,0,1],
  [1,0,1,1,0,1],
  [1,0,1,1,0,2],
  [1,0,1,1,0,1],
]
```

# 📝Instructions
1. Create a function getParkingLotState() that returns an object with totalSlots, availableSlots and occupiedSlots like the following:
const state = {
     totalSlots: 12,
     availableSlots: 3,
     occupiedSlots: 9
}

💡Hints
You have to do a nested loop
