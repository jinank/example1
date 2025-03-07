import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt


file_path = 'flightdata.csv'  # Adjust the file path based on where your file is stored
flight_data = pd.read_csv(file_path)
df = pd.DataFrame(flight_data)

# Display dataset
st.write(df)

df = pd.DataFrame(flight_data)

# Display dataset
st.write("Direct Flights from JFK:")
st.write(df)

filtered_df = df[df.org == 'JFK']

# Create a bar chart
fig = px.bar(filtered_df, x="dest", y="airline", title="Direct Flights from JFK:")

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)    


# Find direct routes from JFK
jfk_direct_routes = df[ (df['origin'] == 'JFK') & (df['dest'] != 'JFK') ][['origin', 'dest']]

# Count the frequency of each destination
destination_counts = jfk_direct_routes['dest'].value_counts()

# Display the unique direct routes
st.write("Unique Direct Routes from JFK:")
st.write(jfk_direct_routes.drop_duplicates())

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 6))
destination_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title('Direct Routes from JFK')
ax.set_xlabel('Destination')
ax.set_ylabel('Number of Flights')
ax.tick_params(axis='x', rotation=45, ha='right')  # Rotate x-axis labels
plt.tight_layout()

# Display the bar chart
st.pyplot(fig)
