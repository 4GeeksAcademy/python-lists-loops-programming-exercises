# Your code here
i = 20
while i >= 1:
    if i % 5 == 0:
        print("%(i)d!"%{"i":i})
    else:
        print(i)
    if i == 1:
        print("LIFTOFF")
    i -= 1
    
    
