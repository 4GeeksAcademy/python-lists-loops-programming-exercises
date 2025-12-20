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
def generate_li(item_color):
    return f"<li>{item_color['label']}</li>"

def filter_colors(all_colors):
    return filter(lambda color:color["sexy"], all_colors)


filteredColors = filter_colors(all_colors)
# print(filteredColors)
    

htmlLi = list(map(generate_li,filteredColors))
print(htmlLi)