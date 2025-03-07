import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Sample dataset of direct flights from JFK
flight_data = {
    'Destination': ['LAX', 'LHR', 'CDG', 'MIA', 'SFO'],
    'Airline': ['American Airlines', 'Delta Air Lines', 'Air France', 'JetBlue Airways', 'United Airlines'],
    'Frequency': [120, 90, 70, 100, 80]
}

df = pd.DataFrame(flight_data)

# Main app
def main():
    st.title("JFK Flight Routes Analysis")
    
    # Sample dataset
    flight_data = {
        'Destination': ['LAX', 'LHR', 'CDG', 'MIA', 'SFO'],
        'Airline': ['American Airlines', 'Delta Air Lines', 'Air France', 'JetBlue Airways', 'United Airlines'],
        'Frequency': [120, 90, 70, 100, 80]
    }
    df = pd.DataFrame(flight_data)
    
    # Display dataset
    st.write("Direct Flights from JFK:")
    st.write(df)
    
    # Draw graph
    fig = draw_graph(df)
    st.pyplot(fig)
    
    # Top destinations by frequency
    top_destinations = df.nlargest(5, 'Frequency')
    st.write("Top 5 Destinations by Frequency:")
    st.write(top_destinations)

if __name__ == "__main__":
    main()
