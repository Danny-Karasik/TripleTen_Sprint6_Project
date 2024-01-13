import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.title('Compare vehicles data')
st.subheader('This app is for the people seeking details about their dream vehicle')

st.caption(':blue[Choose your parameters here!]')

price_range = st.slider("What is your price range?", value = (1,376000))
actual_range = list(range(price_range[0], price_range[1]+1))

newly_listed = st.checkbox('Only newly listed')

if newly_listed:
    filtered_data=data[data.price.isin(actual_range)]
    filtered_date=filtered_data[data.days_listed<=7]
else:
    filtered_data=data[data.price.isin(actual_range)]
    
    
st.write('Here are your options based on your preferences')

fig1 = px.scatter(filtered_data, x="price", y="days_listed")
st.plotly_chart(fig1)

st.write("Distribution of fuel of filtered vehicles")

fig2=px.histogram(filtered_data, x="fuel")
st.plotly_chart(fig2)

st.write('Here is the list of the recommended vehicles')
st.dataframe(filtered_data.sample(10))