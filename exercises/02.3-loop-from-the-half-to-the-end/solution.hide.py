my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

# ❌ ↑ Do NOT change the line of code above ↑ ❌

# ✅ ↓ Your code goes here: ↓ ✅
initialValue = int(len(my_list) / 2) 
stopValue = len(my_list)
increaseValue = 1

# ❌ ↓ Do NOT change any code below this line ↓ ❌

for i in range(initialValue, stopValue, increaseValue):
    print(my_list[i])
