"""
Repeated Choropleth Map
=======================
Three choropleths representing disjoint data from the same table.
"""
# category: geographic

import altair as alt
from vega_datasets import data

pop_eng_hur = alt.UrlData(data.population_engineers_hurricanes.url)

states = alt.UrlData(data.us_10m.url,
                     format=alt.TopoDataFormat(type='topojson',
                                               feature='states'))

variable_list = ['population','engineers','hurricanes']

chart = alt.Chart(states).mark_geoshape().properties(
    projection={'type': 'albersUsa'},
    width=500,
    height=300
).transform_lookup(lookup='id', 
                   from_=alt.LookupData(pop_eng_hur, 'id', variable_list)
).encode(
    color=alt.Color(alt.repeat('row'), type='quantitative')
).repeat(
    row = variable_list
).resolve_scale(color='independent')
