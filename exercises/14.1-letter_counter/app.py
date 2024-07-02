par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
for letra in par:
    if letra != ' ':
        if letra.lower() not in counts:
            counts[letra.lower()] = 1
        else:
            counts[letra.lower()] += 1

print(counts)
