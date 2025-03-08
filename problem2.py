import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(retention_trends['Year'], retention_trends['Retention Rate (%)'])
    ax.set_title('Retention Rate Trends')
    ax.set_xlabel('Year')
    ax.set_ylabel('Retention Rate (%)')
    st.pyplot(fig)
    
    # Plot student satisfaction scores over the years
    st.write("Student Satisfaction Scores Over the Years:")
    satisfaction_trends = analyze_satisfaction_trends(data)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(satisfaction_trends['Year'], satisfaction_trends['Student Satisfaction (%)'])
    ax.set_title('Student Satisfaction Trends')
    ax.set_xlabel('Year')
    ax.set_ylabel('Student Satisfaction (%)')
    st.pyplot(fig)
    
    # Display enrollment breakdown by department
    st.write("Enrollment Breakdown by Department:")
    department_enrollments = analyze_department_enrollments(data)
    st.write(department_enrollments)
    
    # Compare Spring vs. Fall term trends
    st.write("Comparison Between Spring vs. Fall Term Trends:")
    spring_fall_comparison = compare_spring_fall_trends(data)
    st.write(spring_fall_comparison)
    
    # Compare trends between departments, retention rates, and satisfaction levels
    st.write("Comparison of Trends Between Departments, Retention Rates, and Satisfaction Levels:")
    department_trends = data.groupby(['Year'])[['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled', 'Retention Rate (%)', 'Student Satisfaction (%)']].mean()
    st.write(department_trends.reset_index())
    
    # Plot department enrollment trends over time
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(department_trends.index, department_trends['Engineering Enrolled'], label='Engineering')
    ax.plot(department_trends.index, department_trends['Business Enrolled'], label='Business')
    ax.plot(department_trends.index, department_trends['Arts Enrolled'], label='Arts')
    ax.plot(department_trends.index, department_trends['Science Enrolled'], label='Science')
    ax.set_title('Department Enrollment Trends')
    ax.set_xlabel('Year')
    ax.set_ylabel('Enrollment')
    ax.legend()
    st.pyplot(fig)
