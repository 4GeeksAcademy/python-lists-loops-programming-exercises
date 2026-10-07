names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
names[1]="Steven"
arrLen = len(names)
names[arrLen-1] ="Pepe"
names[0]=names[2] + names[4]

for x in range(arrLen-1,-2,-1):
    print(names[x])