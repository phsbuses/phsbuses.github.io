import streamlit as st
import pandas as pd
import numpy as np
from streamlit_sortables import sort_items
import json


# original_items = ['1234', '2345', '3456']

# sorted_items = sort_items(original_items)

# # st.write(f'original_items: {original_items}')
# st.write(f'sorted_items: {sorted_items}')

# while (len(original_items) < 7):
#     original_items.insert(0,'none')

# sorted_items = original_items
# cols = st.columns(len(sorted_items))
# for i, item in enumerate(sorted_items):
#     with cols[i]:
#         st.button(item, key=f"sorted_{i}")

data = [
    {'items':['1234', '2345', '33458979796']},
    {'items':['2341', '2314', '1525']},
    {'items':['----','4567']}
]
sorted = sort_items(data, multi_containers=True)

json_data = json.dumps(sorted)

file_path = "data.json"

with open(file_path, "w") as file:
    file.write(json_data)

with open(file_path, "r") as file:
    json_data = json.load(file)

data = json_data

while (len(data[0]['items']) < 7):
    data[0]['items'].insert(0,'none')
while (len(data[1]['items']) < 7):
    data[1]['items'].insert(0,'none')

items1 = data[0]['items']
cols = st.columns(len(items1))
for i, item in enumerate(items1):
    with cols[i]:
        st.button(item, key=f"sorted1_{i}")

items2 = data[1]['items']
cols = st.columns(len(items2))
for i, item in enumerate(items2):
    with cols[i]:
        st.button(item, key=f"sorted2_{i}")