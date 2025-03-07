import pandas as pd
import plotly.express as px
import streamlit as st

file_path = 'https://github.com/plotly/datasets/blob/master/2011_february_us_airport_traffic.csv'  # Adjust the file path based on where your file is stored
flight_data = pd.read_csv(file_path)
df = pd.DataFrame(flight_data)

# Display dataset
st.write(df)

df = pd.DataFrame(flight_data)

# Display dataset
st.write("Direct Flights from JFK:")
st.write(df)


# Create a bar chart
fig = px.bar(df, x="Destination", y="Airline", title="Direct Flights from JFK:")

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)    
