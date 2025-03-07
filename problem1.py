import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt


file_path = 'flightdata.csv'  # Adjust the file path based on where your file is stored
flight_data = pd.read_csv(file_path)
df = pd.DataFrame(flight_data)

# Find direct routes from JFK.
jfk_direct_routes = df[(df['origin'] == 'JFK') & (df['dest'] != 'JFK')][['origin', 'dest']]

# Count the frequency of each destination.
destination_counts = jfk_direct_routes['dest'].value_counts()

# Display the unique direct routes
st.subheader('Unique Direct Routes from JFK:')
st.write(jfk_direct_routes.drop_duplicates())

# Display the bar chart of direct routes from JFK
st.subheader('Number of Flights to Each Destination from JFK')

plt.figure(figsize=(12, 6))  # Adjust figure size as needed
destination_counts.plot(kind='bar', color='skyblue')
plt.title('Direct Routes from JFK')
plt.xlabel('Destination')
plt.ylabel('Number of Flights')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the chart in Streamlit
st.pyplot(plt)
