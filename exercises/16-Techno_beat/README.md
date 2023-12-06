# `16` Techno Beats

You are working with a DJ, and he needs a program that can create beats for his songs.

## 📝 Instructions:

1. Create a function called `lyrics_generator` that receives a list. The list passed to the function will be something like this:

```py
[0,0,1,1,0,0,0]
```

2. For each Zero you will add to the string `Boom`.

3. For each One you will add to the string `Drop the bass`.

4. **In Addition**, if you find the number `1` three times in a row, you should ALSO ADD to the string `!!!Break the bass!!!`

## 💡 Hints:

- Remember to use auxiliary variables.

- Declare a variable to store the string.

- Declare a variable to count and sum.

## 💻 Expected result:

```py
Boom Boom Drop the bass Drop the bass Boom Boom Boom
Boom Boom Drop the bass Drop the bass Drop the bass !!!Break the bass!!! Boom Boom Boom
Boom Boom Boom
Drop the bass Boom Drop the bass
Drop the bass Drop the bass Drop the bass !!!Break the bass!!!
```
