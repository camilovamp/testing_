import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('vehicles_us.csv')

df['price'] = pd.to_numeric(df['price'], errors='coerce') 
df['price'] = df['price'].fillna(0)  

# Ensure the 'price' column is of type float64
df['price'] = df['price'].astype(float)


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
tableview = selected_manu.style.format({
        'price': '${:,.2f}',  # Format as dollar amount with two decimal places
    }).format({
        'model_year': lambda x: f"{x:.0f}"  # Remove commas from years (treated as float/int)
    })
st.table(tableview)
#st.dataframe(selected_manu)
if select_manu:
    fig1 = px.histogram(selected_manu, x='price', color='manufacturer')
    fig1.update_yaxes(title_text="Number of Vehicles")
    st.plotly_chart(fig1)

# Visualize vehicle price base on mileage on odometer
df['odometer'] = df['odometer'].fillna(value='')
st.header('Vehicle Price by Mileage')
st.write(""" Let's analyze the impact of mileage the odometer and the price of vehicle.""")
fig_odometer_price = px.scatter(df, x='odometer', y='price', labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})
st.write(fig_odometer_price)