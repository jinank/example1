import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
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



# Convert 'dep_time' to datetime if not already done
df['dep_time'] = pd.to_datetime(df['time_hour'])

# Extract the hour of departure
df['dep_hour'] = df['dep_time'].dt.hour

# Group by the hour and count the number of flights
hourly_flight_counts = df.groupby('dep_hour')['origin'].count().reset_index()
hourly_flight_counts.columns = ['Hour of the Day', 'Number of Flights']

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

    st.title("Percentage of Domestic vs. International Flights")
    st.write("This visualization shows the proportion of domestic and international flights.")

    # Calculate percentages
    domestic_flights = df[df['flight_type'] == 'Domestic']
    international_flights = df[df['flight_type'] == 'International']
    
    total_flights = len(df)
    domestic_percentage = (len(domestic_flights) / total_flights) * 100
    international_percentage = (len(international_flights) / total_flights) * 100
    
    # Display percentages
    st.write(f"Percentage of Domestic Flights: {domestic_percentage:.2f}%")
    st.write(f"Percentage of International Flights: {international_percentage:.2f}%")
    
    # Create a pie chart using Plotly Express
    pie_data = pd.DataFrame({
        'Flight Type': ['Domestic', 'International'],
        'Percentage': [domestic_percentage, international_percentage]
    })
    
    fig = px.pie(pie_data, names='Flight Type', values='Percentage',
                 title="Domestic vs. International Flights",
                 color_discrete_sequence=px.colors.sequential.RdBu)
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)

# Streamlit App
def main():
    st.title("Hubs with Significant Traffic Connections")
    st.write("This visualization identifies the top hubs based on flight connections.")

    # Group by destination and count occurrences
    hub_connections = df.groupby('dest')['origin'].count().sort_values(ascending=False).reset_index()
    hub_connections.columns = ['Destination', 'Number of Connections']

    # Display the top hubs
    st.write("Top Hubs with Significant Traffic Connections:")
    st.dataframe(hub_connections.head(10))

    # Identify hubs with more than 5000 connections
    significant_hubs = hub_connections[hub_connections['Number of Connections'] > 5000]
    st.write("\nHubs with More Than 5000 Connections:")
    st.dataframe(significant_hubs)

    # Create a bar chart using Plotly Express
    fig = px.bar(hub_connections.head(10), x='Destination', y='Number of Connections',
                 title="Top Hubs by Number of Connections",
                 labels={'Destination': 'Destination Airport', 'Number of Connections': 'Connections'},
                 color='Number of Connections', color_continuous_scale='Blues')
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()



