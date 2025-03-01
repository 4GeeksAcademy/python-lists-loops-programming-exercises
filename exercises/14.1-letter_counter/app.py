par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
hello = "Hello World"
for letter in par:
    if(letter != " "):
        letter = letter.lower()
        if letter in counts:
            counts[letter] += 1
        elif letter not in counts:
            counts[letter] = 1
    
print(counts)
