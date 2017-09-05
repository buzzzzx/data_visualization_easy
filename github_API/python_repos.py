import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

response_dict = r.json()
items = response_dict['items']

names, stars_dicts = [], []

for item in items:
    names.append(item['name'])

    stars_dict = {
        'value': item['stargazers_count'],
        'label': item['description'],
        'xlink': item['html_url'],
    }
    stars_dicts.append(stars_dict)

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 14
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add("", stars_dicts)

chart.render_to_file('Python_repos.svg')