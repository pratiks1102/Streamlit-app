# tab_numeric/logics.py
import pandas as pd
import altair as alt
import streamlit as st

def calculate_numeric_stats(df, selected_column):
    # Calculate basic statistics
    stats = {
        'Number of Unique Values': df[selected_column].nunique(),
        'Number of Missing Values': df[selected_column].isnull().sum(),
        'Number of Occurrence of 0 Value': (df[selected_column] == 0).sum(),
        'Number of Negative Values': (df[selected_column] < 0).sum(),
        'Average Value': df[selected_column].mean(),
        'Standard Deviation': df[selected_column].std(),
        'Minimum Value': df[selected_column].min(),
        'Maximum Value': df[selected_column].max(),
        'Median Value': df[selected_column].median(),
    }

    return stats

def generate_histogram_chart(df, selected_column):
    # Generate Altair histogram chart
    chart = alt.Chart(df).mark_bar().encode(
        alt.X(selected_column, bin=True),
        y='count()',
    ).properties(
        title=f'Histogram for {selected_column}'
    )

    return chart

def calculate_top_20_values(df, selected_column):
    # Calculate top 20 most frequent values
    top_values = df[selected_column].value_counts().head(20).reset_index()
    top_values.columns = [selected_column, 'Occurrences']
    top_values['Percentage'] = (top_values['Occurrences'] / len(df)) * 100

    return top_values

# Sample usage
# df = pd.read_csv("path/to/your/file.csv")
# selected_column = "your_numeric_column"
# numeric_stats = calculate_numeric_stats(df, selected_column)
# histogram_chart = generate_histogram_chart(df, selected_column)
# top_values = calculate_top_20_values(df, selected_column)
# print(numeric_stats)
# print(top_values)
