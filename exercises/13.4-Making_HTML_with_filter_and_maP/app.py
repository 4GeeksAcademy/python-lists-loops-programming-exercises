all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

filtere_colors = list(filter(lambda color: color["sexy"],all_colors))
result = list(map(lambda color: "<li>"+color["label"]+"</li>", filtere_colors))
print("<ul>" + ''.join(result) + "</ul>")