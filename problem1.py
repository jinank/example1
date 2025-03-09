import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset (replace 'your_dataset.csv' with your actual file name)
df = pd.read_csv('your_dataset.csv')

# Streamlit App
def main():
    st.title("Top 5 Flight Destinations from JFK")
    st.write("This app visualizes the top 5 destinations by number of flights from JFK.")

    # Calculate the top 5 destinations
    top_destinations = df['dest'].value_counts().head(5).reset_index()
    top_destinations.columns = ['Destination', 'Number of Flights']

    # Display the data
    st.write("Top 5 Destinations:")
    st.dataframe(top_destinations)

    # Create a bar chart using Plotly Express
    fig = px.bar(top_destinations, x='Destination', y='Number of Flights', 
                 title='Top 5 Destinations by Number of Flights',
                 labels={'Destination': 'Destination Airport', 'Number of Flights': 'Number of Flights'},
                 color='Number of Flights', color_continuous_scale='Blues')
    
    fig.update_layout(xaxis_title="Destination Airport", 
                      yaxis_title="Number of Flights", 
                      xaxis_tickangle=45)
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
