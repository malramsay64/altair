"""
Gapminder Bubble Plot
=====================
This example shows how to make a bubble plot showing the correlation between health and income for 187 countries in the world (modified from an example in Lisa Charlotte Rost's blog post 'One Chart, Twelve Charting Libraries' --http://lisacharlotterost.github.io/2016/05/17/one-chart-code/).
"""
# category: basic charts

import altair as alt
from vega_datasets import data

gapminder = data.gapminder_health_income.url

chart = alt.Chart(gapminder).mark_circle().encode(
    x = alt.X('income:Q', scale = alt.Scale(type = 'log')),
    y = alt.Y('health:Q', scale = alt.Scale(zero=False)),
    size = 'population:Q'
)
