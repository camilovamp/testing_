import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')


df['price'] = pd.to_numeric(df['price'], errors='coerce') 
df['price'] = df['price'].fillna(0)  

# Ensure the 'price' column is of type float64
df['price'] = df['price'].astype('float64')


df['manufacturer'] = df['model'].str.split().str[0]


st.header("Market Value of Used Vehicles")
st.write(""" Let's look at the price by manufacturer comparison. 
         Select two or more manufacturers to compare prices.
         """)


st.header('Vehicle Price by Manufacturer')
manufacturer_choice = sorted(df['manufacturer'].unique())
select_manu = st.multiselect('Select the manufacturer', manufacturer_choice)
selected_manu = df[df['manufacturer'].isin(select_manu)]


if select_manu:
    st.table(selected_manu)  # Display the table of selected manufacturers
    fig1 = px.histogram(selected_manu, x='price', color='manufacturer')
    fig1.update_yaxes(title_text="Number of Vehicles")
    st.plotly_chart(fig1)


df['odometer'] = df['odometer'].fillna(value='')  
st.header('Vehicle Price by Mileage')
st.write(""" Let's analyze the impact of mileage on the odometer and the price of the vehicle.""")
fig_odometer_price = px.scatter(df, x='odometer', y='price', labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})
st.write(fig_odometer_price)
