import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("My App")

st.write("Creating a table")
city_data = pd.DataFrame({
    "City": ["New York", "Los Angeles", "Chicago"],
    "Population": [15_000_000, 20_000_000, 5_000_000]
    })
st.write(city_data)

st.write("Creating a table with st.dataframe with some random data")
df = pd.DataFrame(
    np.random.randn(100, 10),
    columns=(['column_' + str(i) for i in range(10)])
)
st.dataframe(df)

st.write("DataFrame with magic methods")
df_2 = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df_2
st.write("Adding an option box (purpose unknown yet)")
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df_2['first column'])

'You selected: ', option

st.write("Draw a line chart")
chart_data = pd.DataFrame(
    np.random.randn(50,3),
    columns=['col_a', 'col_b', 'col_c']
)
st.line_chart(chart_data)

st.write("Plot a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)
st.write("Conditional showing data with checkboxes")
if st.checkbox("Show raw coordinates?"):
    map_data

st.write("Using columns with buttons for interaction and output")
button_column, response_column = st.columns(2)
pressed = button_column.button('Press the button')
if pressed:
  response_column.write("Woohoo!")

st.write("Adding dropdown expander")
expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
for explanation in ["A", "B", "C", "D", "E"]:
    expander.write(f"Explanation {explanation} ...")

st.write("Adding a progress bar")
latest = st.empty()
bar = st.progress(0)

for i in range(100):
    latest.text(f"Loading {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.2)