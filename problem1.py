import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('jfk_flight_routes.csv')

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


# Convert 'dep_time' to datetime if not already done
df['dep_time'] = pd.to_datetime(df['time_hour'])

# Extract the hour of departure
df['dep_hour'] = df['dep_time'].dt.hour

# Group by the hour and count the number of flights
hourly_flight_counts = df.groupby('dep_hour')['origin'].count().reset_index()
hourly_flight_counts.columns = ['Hour of the Day', 'Number of Flights']

# Streamlit App
def main():
    st.title("Flight Volume by Time of Day")
    st.write("This visualization shows the distribution of flight volume across different hours of the day.")

    # Display the data table
    st.write("Hourly Flight Volume:")
    st.dataframe(hourly_flight_counts)

    # Create an interactive line chart using Plotly Express
    fig = px.line(hourly_flight_counts, x='Hour of the Day', y='Number of Flights',
                  title="Flight Volume by Time of Day",
                  labels={'Hour of the Day': 'Hour', 'Number of Flights': 'Number of Flights'},
                  markers=True)
    
    fig.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=1),  # Ensure all hours are displayed on x-axis
                      yaxis_title="Number of Flights",
                      xaxis_title="Hour of the Day")
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
