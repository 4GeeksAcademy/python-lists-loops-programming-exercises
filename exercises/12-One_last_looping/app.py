my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

my_sample_list[1] == "Steve"
my_sample_list[-1] == "Pepe"
my_sample_list[0] == my_sample_list[2] + my_sample_list[4]


for i in reversed(my_sample_list):
    print(i)


new_list = []
for i in range(len(my_sample_list)):
    new_list.append(my_sample_list[-i-1])
print(new_list)