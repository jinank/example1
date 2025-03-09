import streamlit as st
import pandas as pd
import plotly.express as px

# First, we will load the dataset from uscrime.csv file
df = pd.read_csv('uscrime.csv', index_col=0)

def main():
    st.title("Crime Data Analysis: Worst vs. Improved Visualizations")
    st.write("This app demonstrates poorly designed (worst) and improved visualizations for analyzing crime data.")

    # In this problem, we will create a sidebar for navigation with options to choose from
    st.sidebar.title("Navigation")
    options = ["Worst Plot 1", "Improved Plot 1", "Worst Plot 2", "Improved Plot 2"]
    choice = st.sidebar.radio("Select Visualization", options)

    if choice == "Worst Plot 1":
        st.subheader("Worst Visualization 1")
        st.write("This visualization is cluttered and difficult to interpret, with overlapping lines and redundant elements.")
        
        # Now, we will create WORST Possible Plot 1: Overlapping lines and scatter points
        fig = px.scatter(df, x='Murder', y='Assault', title="Relationship Between Murder and Assault Rates (Bad Plot)",
                         color_discrete_sequence=['red'])
        fig.add_scatter(x=df['Murder'], y=df['Assault'], mode='lines', line=dict(color='blue'))
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

    elif choice == "Improved Plot 1":
        st.subheader("Improved Visualization 1")
        st.write("This scatter plot with a regression line provides clarity and insight into the relationship.")
        
        # Next, we will create Improved Plot 1: Scatter plot with regression line
        fig = px.scatter(df, x='Murder', y='Assault', trendline="ols",
                         title="Relationship Between Murder and Assault Rates (Improved)",
                         labels={'Murder': 'Murder Rate', 'Assault': 'Assault Rate'})
        st.plotly_chart(fig)

    elif choice == "Worst Plot 2":
        st.subheader("Worst Visualization 2")
        st.write("This visualization uses unnecessary connections between points, creating a web-like structure that is visually overwhelming.")
        
        # Again, we will create another WORST Possible Plot 2: Web-like structure connecting points
        fig = px.line(df, x='Murder', y='Assault', title="Relationship Between Murder and Assault Rates (Bad Plot)",
                      markers=True)
        fig.update_traces(line=dict(color='blue'), marker=dict(size=8))
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

    elif choice == "Improved Plot 2":
        st.subheader("Improved Visualization 2")
        st.write("This scatter plot uses size and color to add depth to the data while maintaining clarity.")
        
        # And to compare the WORST plot 2, we will create Improved Plot 2: Scatter plot with size and color encoding
        fig = px.scatter(df, x='Murder', y='Assault', size='Rape', color='UrbanPop',
                         title="Relationship Between Murder and Assault Rates",
                         labels={'Murder': 'Murder Rate', 'Assault': 'Assault Rate'},
                         color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
