arr = [45, 67, 87, 23, 5,  32, 60]

# ❌ ↑ Do NOT change the line of code above ↑ ❌

# ✅ ↓ Your code goes here: ↓ ✅

new_list = []
# 🚨 Be aware that there are other solutions 🚨
for n in arr[::-1]:       
    new_list.append(n)

print(new_list)