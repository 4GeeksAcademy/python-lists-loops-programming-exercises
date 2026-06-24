all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]


def filter_colors(colors):
    return list(filter(lambda color: color["sexy"], colors))

def generate_li(colors):
    return list(map(lambda color: f"<li>{color['label']}</li>", colors))


filtered = filter_colors(all_colors)
html_list = generate_li(filtered)
print(html_list)