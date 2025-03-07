import pandas as pd
import plotly.express as px
import streamlit as st

file_path = 'usa_air_traffic.csv'  # Adjust the file path based on where your file is stored
flight_data = pd.read_csv(file_path)
print(flight_data.head())


st.title("First")
df = pd.DataFrame(flight_data)

# Display dataset
st.write("First")
st.write(df)


# Sample dataset of direct flights from JFK
flight_data = {
    'Destination': ['LAX', 'LHR', 'CDG', 'MIA', 'SFO'],
    'Airline': ['American Airlines', 'Delta Air Lines', 'Air France', 'JetBlue Airways', 'United Airlines'],
    'Frequency': [120, 90, 70, 100, 80]
}

st.title("JFK Flight Routes Analysis")
df = pd.DataFrame(flight_data)

# Display dataset
st.write("Direct Flights from JFK:")
st.write(df)


# Create a bar chart
fig = px.bar(df, x="Destination", y="Airline", title="Direct Flights from JFK:")

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)    
