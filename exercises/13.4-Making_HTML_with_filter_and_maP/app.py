all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def filter_colors(color):
    return color["sexy"] == True

def generate_li(color):
    new_li = f'<li>{color["label"]}</li>'
    return new_li

sexy_colors = list(filter(filter_colors,all_colors))
print (sexy_colors)

html_list = list(map(generate_li,sexy_colors))
print(html_list)