import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt


file_path = 'flightdata.csv'  # Adjust the file path based on where your file is stored
flight_data = pd.read_csv(file_path)
df = pd.DataFrame(flight_data)

# Display dataset
st.write(df)

# Display dataset
st.write("Direct Flights from JFK:")

# Display the Plotly chart in Streamlit
fig = px.bar(df, x="dest", y="airline", title=" Flights from JFK")

st.plotly_chart(fig)    

# Find direct routes from JFK
jfk_direct_routes = df[ (df['origin'] == 'JFK') & (df['dest'] != 'JFK') ][['origin', 'dest']]

# Count the frequency of each destination
destination_counts = jfk_direct_routes['dest'].value_counts()

# Display the unique direct routes
st.write("Unique Direct Routes from JFK:")
st.write(jfk_direct_routes.drop_duplicates())

# Create the bar chart
destination_counts.plot(kind='bar', color='skyblue')
# Display the bar chart
st.plotly_chart(fig)
