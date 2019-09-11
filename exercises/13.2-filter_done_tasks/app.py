tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]




#using function
def my_function(items):
    return items['done']
result = list(filter(my_function, tasks))
print(result)

#lambda expretion
done_tasks = list(filter(lambda x: x['done'], tasks))
print(done_tasks)