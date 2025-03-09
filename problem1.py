import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('jfk_flight_routes.csv')

# Streamlit App
def main():
    st.title("JFK Flight Route Analysis")
    st.write("Explore flight routes, volumes, and trends from JFK airport.")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = [
        "Direct Routes from JFK",
        "Top 5 Destinations by Flights",
        "Flight Volume by Time of Day",
        "Domestic vs. International Flights",
        "Hubs with Significant Traffic Connections",
        "Most Frequent Airlines from JFK"
    ]
    choice = st.sidebar.radio("Select Analysis", options)

    if choice == "Direct Routes from JFK":
        st.subheader("Direct Routes from JFK")
        
        # Direct routes and their counts
        jfk_direct_routes = df[(df['origin'] == 'JFK') & (df['dest'] != 'JFK')][['origin', 'dest']]
        destination_counts = jfk_direct_routes['dest'].value_counts()
        
        # Combine with flight counts
        jfk_direct_routes_counts = jfk_direct_routes.drop_duplicates().copy()
        jfk_direct_routes_counts['num_flights'] = jfk_direct_routes_counts['dest'].map(destination_counts)
        
        # Display the data
        st.write(jfk_direct_routes_counts)
        
        # Bar chart using Plotly Express
        fig = px.bar(destination_counts.reset_index(), x='index', y='dest',
                     title='Direct Routes from JFK',
                     labels={'index': 'Destination', 'dest': 'Number of Flights'},
                     color='dest', color_continuous_scale='Blues')
        st.plotly_chart(fig)

    elif choice == "Top 5 Destinations by Flights":
        st.subheader("Top 5 Destinations by Number of Flights")
        
        # Calculate top 5 destinations
        top_destinations = df['dest'].value_counts().head(5).reset_index()
        top_destinations.columns = ['Destination', 'Number of Flights']
        
        # Display the data
        st.write(top_destinations)
        
        # Bar chart using Plotly Express
        fig = px.bar(top_destinations, x='Destination', y='Number of Flights',
                     title='Top 5 Destinations by Number of Flights',
                     color='Number of Flights', color_continuous_scale='Blues')
        st.plotly_chart(fig)

    elif choice == "Flight Volume by Time of Day":
        st.subheader("Flight Volume by Time of Day")
        
        # Extract hour and group by hour
        df['dep_time'] = pd.to_datetime(df['dep_time'])
        df['dep_hour'] = df['dep_time'].dt.hour
        hourly_flight_counts = df.groupby('dep_hour')['origin'].count().reset_index()
        
        # Line chart using Plotly Express
        fig = px.line(hourly_flight_counts, x='dep_hour', y='origin',
                      title="Flight Volume by Time of Day",
                      labels={'dep_hour': 'Hour of the Day', 'origin': 'Number of Flights'})
        st.plotly_chart(fig)

    elif choice == "Domestic vs. International Flights":
        st.subheader("Percentage of Domestic vs. International Flights")
        
        # Calculate percentages
        domestic_flights = df[df['flight_type'] == 'Domestic']
        international_flights = df[df['flight_type'] == 'International']
        
        total_flights = len(df)
        domestic_percentage = (len(domestic_flights) / total_flights) * 100
        international_percentage = (len(international_flights) / total_flights) * 100
        
        # Display percentages
        st.write(f"Percentage of Domestic Flights: {domestic_percentage:.2f}%")
        st.write(f"Percentage of International Flights: {international_percentage:.2f}%")
        
        # Pie chart using Plotly Express
        pie_data = pd.DataFrame({
            'Flight Type': ['Domestic', 'International'],
            'Percentage': [domestic_percentage, international_percentage]
        })
        
        fig = px.pie(pie_data, names='Flight Type', values='Percentage',
                     title="Domestic vs. International Flights",
                     color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig)

     
