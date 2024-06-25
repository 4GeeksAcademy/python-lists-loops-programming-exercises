names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
names[1] = 'Steven'
names[-1] = 'Pepe'
names[0] = 'Ruth'+'Pedro'

for i in range(len(names), -1, -1):
    print(names[i-1])