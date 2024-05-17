my_sample_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

# Modify the loop below to print from end to start

for i in range(len(my_sample_list) -1, -1, -1):
    print(my_sample_list[i])

# for i in range (desde dónde empezamos, hasta donde llegamos, hacia donde y cuanto)
# (último elemento de array, hasta donde llegamos, hacia donde y cada cuanto)
# último elemento: será la longitud del array, y para referirnos al último elemento -1
# hasta donde: pensamos hasta donde queremos llegar, en este caso 0, y hacemos -1, porque lee un núm antes
# hacia dónde: queremos que cuente de uno en uno: 1. Pero queremos que vaya hacia atrás: -1

