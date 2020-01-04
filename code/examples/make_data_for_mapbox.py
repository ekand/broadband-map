### notes: this created a ~100 MB file of geojson for cook county (I think?)


# opens a geojson file that I got from the us census website
# pu it into 


import json
import random

with open('tl_2018_17_tabblock10.geojson') as jsonfile:
    geo_data = json.load(jsonfile)


geo_data_keep = {
"type": "FeatureCollection",
"name": "tl_2018_17_tabblock10",
"features": []
}

for feature in geo_data['features']:
    county_code = feature['properties']['COUNTYFP10']
    if county_code == '031':
        geo_data_keep['features'].append(feature)

for feature in geo_data_keep['features']:
    properties = feature['properties']
    properties['random_data'] = random.randint(1, 101)


with open('geo_data_cook_county_with_random.txt', 'w') as outfile:
    json.dump(geo_data_keep, outfile)

"""

with open('tl_2018_17_tabblock10.geojson') as jsonfile:
    geo_data = json.load(jsonfile)

features_df = pd.DataFrame(geo_data['features'])

for i in range(451554):
    d = features_df
.iloc[i].loc['properties']
    d['SPEED'] = random.random()


features_df.to_json('full_blocks_with_fake_speed.json')

"""
"""
    my_list = []
    for entry in foo['properties']:
        my_list.append(entry['GEOID10'])

    my_list = my_list[:100]

    with open('temp_data.txt', 'w') as file:
        file.write(my_list)

if False:
    with open('temp_data.txt', 'r') as file:
        my_list = list(file.read())


print('foo')
f = pd.Series(my_list)
c = pd.DataFrame(f)
c[1] = f
d = pd.DataFrame(c, columns=['zero', 'one'])





m = folium.Map(
    location = [ 40.817236, -89.650537],
    zoom_start = 15
)

geo_data_filename = 'tl_2018_17_tabblock10.geojson'

folium.Choropleth(
    geo_data=geo_data_filename,
    name='choropleth',
    data=d,
    columns=['zero', 'one'],
    key_on='feature.properties.GEOID10',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=.5,
    legend_name='Arbitrary Numbers'
).add_to(m)

m.save('geo_data_full_fake_numbers.html')
"""