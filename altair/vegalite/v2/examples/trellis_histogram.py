"""
Trellis Histogram
-----------------
This example shows how to make a basic trellis histogram.
https://vega.github.io/vega-lite/examples/trellis_bar_histogram.html
"""
import altair as alt

cars = alt.load_dataset('cars')

chart = alt.Chart(cars).mark_bar().encode(
    alt.X("Horsepower",
          type="quantitative",
          bin=alt.Bin(maxbins=15)),
    y='count(*):Q',
    row='Origin'
)
