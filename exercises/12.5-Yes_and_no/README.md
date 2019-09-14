#`12.5` Yes and no

#📝Instructions
1. Please use the list map functionality to loop the list of booleans and create a new list
 that contains the string 'wiki' for every 1 and 'woko' for every 0 that the original list had.
2. Print that list on the console.

```py
Example output:

[ 'woko',   'wiki',   'woko',   'woko',   'wiki',   'wiki',   'wiki',   'woko',   'woko',   'wiki',   'woko',   'wiki',   'wiki',   'woko',   'woko',   'woko',   'woko',   'woko',   'woko',   'woko',   'woko',   'wiki',   'woko',   'woko',   'woko',   'woko',   'wiki' ]
```

Hint
You need to map the entire list
Inside your mapping function you need to use a conditional to verify if the current value is 0 or 1.
If the current value is 1 you print the string 'wiki'
If the current value is 0 you print the string 'woko'