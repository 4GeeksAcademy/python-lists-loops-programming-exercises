my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

my_sample_list[1] = "Steve"
my_sample_list[-1] = "Pepe"
my_sample_list[0] = my_sample_list[2] + my_sample_list[4]


new_list = []
for names in range(len(my_sample_list)):
    new_list.append(my_sample_list[-names-1])
print('\n'.join(new_list))
