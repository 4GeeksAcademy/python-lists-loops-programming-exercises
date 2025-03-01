names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
for i in range(len(names)-1,-1,-1):
    if len(names)-1 == i:
        names[i]="Pepe"
    elif i==1:
        names[i]="Steven"
    elif i == 0:
        names[i]=names[2]+names[4]
    print(names[i])
    