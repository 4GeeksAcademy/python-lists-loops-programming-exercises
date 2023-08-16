#  import the random package here ✅ ↓ "import random" ↓ ✅
import random

# ❌ ↓  Do NOT change the code below this line ↓ ❌
def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = generate_random_list() 

# ❌ ↑ Do NOT change the code above this line ↑ ❌

# ✅ ↓ Feel happy to write the code below this comment, good luck!: ↓ ✅
the_last_one = my_stupid_list[-1]
print(the_last_one)
