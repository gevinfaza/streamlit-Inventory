import streamlit as st
import pandas as pd
import plotly.express as px


dataset = pd.read_csv("inventories_update.csv")
# Sidebar
# Date Control
st.sidebar.header("Date Control")


year = st.sidebar.multiselect(
    "Select Year",
    options=dataset['Purchase_Year'].unique(),
    default=dataset['Purchase_Year'].unique()
)

# data control
st.sidebar.header("Data Control")

category = st.sidebar.multiselect(
    "Select Category",
    options=dataset['Category'].unique(),
    default=dataset['Category'].unique()
)

location = st.sidebar.multiselect(
    "Select Location",
    options=dataset['Location'].unique(),
    default=dataset['Location'].unique()
)

condition = st.sidebar.multiselect(
    "Select Condition",
    options=dataset['Condition'].unique(),
    default=dataset['Condition'].unique()
)

# filter data
data = dataset.query("Purchase_Year == @year & Category == @category & Location == @location & Condition == @condition ")

st.title("PT.Rumah Media Interaksi")

# KPI
sum_item = int(data['Quantity'].sum())
sum_asset = int(data['Value'].sum())
max = int(data['Price'].max())
min = int(data['Price'].min())

total_items = format (sum_item, ",")
total_asset =format (sum_asset, ",")
max_asset =format (max, ",")
min_asset =format (min, ",")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Item")
    st.subheader(total_items) 
with col2:
    st.subheader("Total Asset ")
    st.subheader(total_asset)


with col3:
    st.subheader("Highest Asset")
    st.subheader(max_asset) 


with col4:
    st.subheader("Lowest Asset")
    st.subheader(min_asset) 

#Bar Chart
df = pd.DataFrame(data)

results_type = st.selectbox('Value', ['Category', 'Location', 'Condition'] )
output_columns = ['Value']
df_grouped = df.groupby(by=[results_type], as_index=False)[output_columns].sum()


fig = px.bar(df_grouped, x=results_type, y='Value', color='Value', 
             color_continuous_scale=['red', 'yellow', 'green'],
             template='plotly_white', title=f'<b>Value by {results_type}</b>')

st.plotly_chart(fig)

# Line Chart
df = pd.DataFrame(data)
results_type = st.selectbox('Value', ['Purchase_Year'] )
output_columns = ['Value']
df_grouped = df.groupby(by=[results_type], as_index=False)[output_columns].sum()


fig = px.line(df_grouped, x=results_type, y='Value', title=f'<b>Value by {results_type}</b>')

st.plotly_chart(fig)


#Pie Chart Category

df = pd.DataFrame(data)

pie1, pie2 = st.columns(2)

with pie1:
    results_type = st.selectbox('Category', ['Quantity'])
    
    fig = px.pie(df, values=results_type, names='Category',
                 title= f'<b>Category by {results_type}</b>',
                 height=300, width=200)
    st.plotly_chart(fig, use_container_width=True)

#Pie Chart Location

df = pd.DataFrame(data)

with pie2:
    results_type = st.selectbox('Location', ['Quantity'])
    
    fig = px.pie(df, values=results_type, names='Location',
                 title= f'<b>Location by {results_type}</b>',
                 height=300, width=200)
    st.plotly_chart(fig, use_container_width=True)

