import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('university_student_dashboard_data.csv')

# Function to calculate total applications, admissions, and enrollments per term
def calculate_term_metrics(data):
    term_metrics = data.groupby(['Year', 'Term'])[['Applications', 'Admitted', 'Enrolled']].sum()
    return term_metrics.reset_index()

# Function to analyze retention rate trends over time
def analyze_retention_trends(data):
    retention_trends = data.groupby(['Year'])['Retention Rate (%)'].mean()
    return retention_trends.reset_index()

# Function to analyze student satisfaction scores over the years
def analyze_satisfaction_trends(data):
    satisfaction_trends = data.groupby(['Year'])['Student Satisfaction (%)'].mean()
    return satisfaction_trends.reset_index()

# Function to analyze enrollment breakdown by department
def analyze_department_enrollments(data):
    department_enrollments = data.groupby(['Year', 'Term'])[['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']].sum()
    return department_enrollments.reset_index()

# Function to compare Spring vs. Fall term trends
def compare_spring_fall_trends(data):
    spring_fall_comparison = data.groupby(['Term'])[['Applications', 'Admitted', 'Enrolled', 'Retention Rate (%)', 'Student Satisfaction (%)']].mean()
    return spring_fall_comparison.reset_index()

# Function to compare trends between departments, retention rates, and satisfaction levels
def compare_department_trends(data):
    department_trends = data.groupby(['Year'])[['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled', 'Retention Rate (%)', 'Student Satisfaction (%)']].mean()
    return department_trends.reset_index()

# Main app
def main():
    st.title("University Student Dashboard")
    
    # Display total applications, admissions, and enrollments per term
    st.write("Total Applications, Admissions, and Enrollments per Term:")
    term_metrics = calculate_term_metrics(data)
    st.write(term_metrics)
    
    # Plot retention rate trends over time
    st.write("Retention Rate Trends Over Time:")
    retention_trends = analyze_retention_trends(data)
    fig = px.line(retention_trends, x='Year', y='Retention Rate (%)', title='Retention Rate Trends')
    st.plotly_chart(fig, use_container_width=True)
    
    # Plot student satisfaction scores over the years
    st.write("Student Satisfaction Scores Over the Years:")
    satisfaction_trends = analyze_satisfaction_trends(data)
    fig = px.line(satisfaction_trends, x='Year', y='Student Satisfaction (%)', title='Student Satisfaction Trends')
    st.plotly_chart(fig, use_container_width=True)
    
    # Display enrollment breakdown by department
    st.write("Enrollment Breakdown by Department:")
    department_enrollments = analyze_department_enrollments(data)
    st.write(department_enrollments)
    
    # Plot department enrollment trends over time
    st.write("Department Enrollment Trends Over Time:")
    department_trends = compare_department_trends(data)
    fig = px.line(department_trends, x='Year', y=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled'], title='Department Enrollment Trends')
    st.plotly_chart(fig, use_container_width=True)
    
    # Compare Spring vs. Fall term trends
    st.write("Comparison Between Spring vs. Fall Term Trends:")
    spring_fall_comparison = compare_spring_fall_trends(data)
    st.write(spring_fall_comparison)
    
    # Plot comparison between Spring and Fall terms
    st.write("Spring vs. Fall Term Comparison:")
    fig = px.bar(spring_fall_comparison, x='Term', y=['Applications', 'Admitted', 'Enrolled'], barmode='group', title='Spring vs. Fall Term Trends')
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
