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

# Main app
def main():
    st.title("University Student Dashboard")
    
    ax.set_ylabel('Enrollment')
    ax.legend()
    st.plotly_chart(fig)
