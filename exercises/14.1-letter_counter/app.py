par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here

for charac in par :
    charac = charac.lower()
    if charac == ' ':
        continue
    if charac in counts:
        counts[charac] += 1
    else:
        counts[charac] = 1


print(counts)
