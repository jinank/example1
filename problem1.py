import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

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

# Draw graph
fig = draw_graph(df)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)    
