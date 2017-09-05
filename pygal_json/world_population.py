import json
from countries_codes import get_country_code
import pygal
from pygal.style import RotateStyle

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
cc_1, cc_2, cc_3 = {}, {}, {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_1[cc] = pop
    elif pop < 1000000000:
        cc_2[cc] = pop
    else:
        cc_3[cc] = pop


wm_style = RotateStyle('#336699')
wm = pygal.Worldmap(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", cc_1)
wm.add("10m-1bn", cc_2)
wm.add(">1bn", cc_3)
wm.render_to_file('world_population.svg')
