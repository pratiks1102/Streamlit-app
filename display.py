# tab_numeric/display.py
import streamlit as st
import pandas as pd
import altair as alt

def display_numeric_tab(df):
    st.title("Numeric Serie Tab")

    # Detect numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    # Display selection box for numeric columns
    selected_column = st.selectbox("Select Numeric Column", numeric_columns)

    # Display basic statistics as a static table
    st.write(f"### Basic Statistics for {selected_column}")
    stats_table = pd.DataFrame({
        'Number of Unique Values': [df[selected_column].nunique()],
        'Number of Missing Values': [df[selected_column].isnull().sum()],
        'Number of Occurrence of 0 Value': [(df[selected_column] == 0).sum()],
        'Number of Negative Values': [(df[selected_column] < 0).sum()],
        'Average Value': [df[selected_column].mean()],
        'Standard Deviation': [df[selected_column].std()],
        'Minimum Value': [df[selected_column].min()],
        'Maximum Value': [df[selected_column].max()],
        'Median Value': [df[selected_column].median()],
    })

    st.table(stats_table)

  
    st.write(f"### Histogram for {selected_column}")
    chart = alt.Chart(df).mark_bar().encode(
        alt.X(selected_column, bin=True),
        y='count()',
    ).properties(
        title=f'Histogram for {selected_column}'
    )
    st.altair_chart(chart, use_container_width=True)

    # Table for top 20 most frequent values
    st.write(f"### Top 20 Most Frequent Values for {selected_column}")
    top_values = df[selected_column].value_counts().head(20).reset_index()
    top_values.columns = [selected_column, 'Occurrences']
    top_values['Percentage'] = (top_values['Occurrences'] / len(df)) * 100
    st.table(top_values)

