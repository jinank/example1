import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# Sample dataset of direct flights from JFK
flight_data = {
    'Destination': ['LAX', 'LHR', 'CDG', 'MIA', 'SFO'],
    'Airline': ['American Airlines', 'Delta Air Lines', 'Air France', 'JetBlue Airways', 'United Airlines'],
    'Frequency': [120, 90, 70, 100, 80]
}

df = pd.DataFrame(flight_data)

# Create a directed graph
G = nx.DiGraph()

# Add JFK as the source node
G.add_node('JFK')

# Add destinations and edges
for index, row in df.iterrows():
    G.add_node(row['Destination'])
    G.add_edge('JFK', row['Destination'])

# Draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=5000, edge_color='gray')
plt.show()

import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Function to draw the graph
def draw_graph(df):
    G = nx.DiGraph()
    G.add_node('JFK')
    
    for index, row in df.iterrows():
        G.add_node(row['Destination'])
        G.add_edge('JFK', row['Destination'])
        
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw_networkx(G, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=5000, edge_color='gray')
    return fig

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
