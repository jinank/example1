import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('jfk_flight_routes.csv')

def main():
    st.title("Top 5 Flight Destinations from JFK")
    st.write("This app visualizes the top 5 destinations by number of flights from JFK.")

    # We will calculate the top 5 destinations
    top_destinations = df['dest'].value_counts().head(5).reset_index()
    top_destinations.columns = ['Destination', 'Number of Flights']

    # Than, we will display the data
    st.write("Top 5 Destinations:")
    st.dataframe(top_destinations)

    # After that, we will create a bar chart using Plotly Express
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

df['dep_time'] = pd.to_datetime(df['time_hour'])
df['dep_hour'] = df['dep_time'].dt.hour

# We will group by the hour and count the number of flights
hourly_flight_counts = df.groupby('dep_hour')['origin'].count().reset_index()
hourly_flight_counts.columns = ['Hour of the Day', 'Number of Flights']

def main():
    st.title("Flight Volume by Time of Day")
    st.write("This visualization shows the distribution of flight volume across different hours of the day.")

    # Than, we will display the data
    st.write("Hourly Flight Volume:")
    st.dataframe(hourly_flight_counts)

    # After that, we will create an interactive line chart using Plotly Express
    fig = px.line(hourly_flight_counts, x='Hour of the Day', y='Number of Flights',
                  title="Flight Volume by Time of Day",
                  labels={'Hour of the Day': 'Hour', 'Number of Flights': 'Number of Flights'},
                  markers=True)
    
    fig.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=1),  # Ensure all hours are displayed on x-axis
                      yaxis_title="Number of Flights",
                      xaxis_title="Hour of the Day")
    
    # Than, we will display chart in streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()


def main():
    st.title("Percentage of Domestic vs. International Flights")
    st.write("This visualization shows the proportion of domestic and international flights.")

    # First, we will calculate percentages
    domestic_flights = df[df['flight_type'] == 'Domestic']
    international_flights = df[df['flight_type'] == 'International']
    
    total_flights = len(df)
    domestic_percentage = (len(domestic_flights) / total_flights) * 100
    international_percentage = (len(international_flights) / total_flights) * 100
    
    # We will display percentages
    st.write(f"Percentage of Domestic Flights: {domestic_percentage:.2f}%")
    st.write(f"Percentage of International Flights: {international_percentage:.2f}%")
    
    # After that, we will create a pie chart using Plotly Express
    pie_data = pd.DataFrame({
        'Flight Type': ['Domestic', 'International'],
        'Percentage': [domestic_percentage, international_percentage]
    })
    
    fig = px.pie(pie_data, names='Flight Type', values='Percentage',
                 title="Domestic vs. International Flights",
                 color_discrete_sequence=px.colors.sequential.RdBu)
    
    # Finally, we will display the chart in streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()


def main():
    st.title("Hubs with Significant Traffic Connections")
    st.write("This visualization identifies the top hubs based on flight connections.")

    # Here we will group by destination and count occurrences
    hub_connections = df.groupby('dest')['origin'].count().sort_values(ascending=False).reset_index()
    hub_connections.columns = ['Destination', 'Number of Connections']

    # We will display the top hubs
    st.write("Top Hubs with Significant Traffic Connections:")
    st.dataframe(hub_connections.head(10))

    # Thanm, identify hubs with more than 5000 connections
    significant_hubs = hub_connections[hub_connections['Number of Connections'] > 5000]
    st.write("\nHubs with More Than 5000 Connections:")
    st.dataframe(significant_hubs)

    # And than, create a bar chart using Plotly Express
    fig = px.bar(hub_connections.head(10), x='Destination', y='Number of Connections',
                 title="Top Hubs by Number of Connections",
                 labels={'Destination': 'Destination Airport', 'Number of Connections': 'Connections'},
                 color='Number of Connections', color_continuous_scale='Blues')
    
    # Finally, display the chart in streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

def main():
    st.title("Most Frequent Airlines Operating from JFK")
    st.write("This visualization identifies the airlines with the highest number of flights from JFK.")

    # First, we will count the frequency of each airline
    airline_counts = df['airline'].value_counts().reset_index()
    airline_counts.columns = ['Airline', 'Number of Flights']

    # And than, display the most frequent airlines
    st.write("\nTop 10 Most Frequent Airlines Operating from JFK:")
    st.dataframe(airline_counts.head(10))

    # After that, we will create a bar chart using Plotly Express
    fig = px.bar(airline_counts.head(10), x='Airline', y='Number of Flights',
                 title="Most Frequent Airlines from JFK",
                 labels={'Airline': 'Airline', 'Number of Flights': 'Number of Flights'},
                 color='Number of Flights', color_continuous_scale='Blues')
    
    fig.update_layout(xaxis_tickangle=45)  # Rotate x-axis labels for better readability
    
    # At last, we will display the chart in Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
