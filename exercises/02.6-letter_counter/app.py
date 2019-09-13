par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

#Your code go here:

count = {}
for i in par:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

