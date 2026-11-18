par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
for char in par.lower():
    if char.isalpha():  # Ignora espacios y signos
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1


print(counts)
