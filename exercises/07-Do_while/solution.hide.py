# Your code here

number = 20

while number >= 1: # El bucle while se hace siempre y cuando el número sea más grande o igual que 1
    if number % 5 == 0:
        print(str(number) + "!")
    else:
        print(number)
    number -= 1

print("LIFTOFF")
