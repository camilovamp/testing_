import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')
df['price'] = df['price'].astype(float)

#df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
df['manufacturer'] = df['model'].str.split().str[0]

# create a data viewer
st.header("Market Value of Used Vehicles")
st.write(""" Let's look at the price by manufacturer comparison. 
         Select two or more manufacture to compare price.
         """)

# visualize vehicle price by manufacturer
st.header('Vehicle Price by Manufacturer')
manufacturer_choise = sorted(df['manufacturer'].unique())
select_manu = st.multiselect('Select the manufacturer',manufacturer_choise)
selected_manu = df[df['manufacturer'].isin(select_manu)]
selected_manu
if select_manu:
    fig1 = px.histogram(selected_manu, x='price', color='manufacturer')
    fig1.update_yaxes(title_text="Number of Vehicles")
    st.plotly_chart(fig1)

# Visualize vehicle price base on mileage on odometer
df['price'] = df['price'].astype('float')
df['odometer'] = df['odometer'].fillna(value='')
st.header('Vehicle Price by Mileage')
st.write(""" Let's analyze the impact of mileage the odometer and the price of vehicle.""")
fig_odometer_price = px.scatter(df, x='odometer', y='price', labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})
st.write(fig_odometer_price)

