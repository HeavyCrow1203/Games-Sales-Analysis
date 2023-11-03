import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Dashboard Game Sales",
    layout="wide"
)

# load data
df = pd.read_csv('H:\Code-Program\python\Data Analysis\Game Analysis\Games Sales.csv')

# drop data duplicates
df = df.drop_duplicates()
df.duplicated().sum()

# change datatype in release column to datetime
df['Release'] = pd.to_datetime(df['Release'])
df.info()

# drop NaN value in series column
df = df.dropna(subset=['Series'])
df.isna().sum()

print(df.head(5))

st.title("Dashboard Games Sales")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Games", df.shape[0])
col2.metric("Total Series", df.Series.nunique())
col3.metric("Total Genre", df.Genre.nunique())
col4.metric("Total Developer", df.Developer.nunique())
col5.metric("Total Publisher", df.Publisher.nunique())

a1, a2 = st.columns(2)
with a1:
    selectbox_options = [col for col in df.columns if col not in ['Name','Sales', 'Release']]
    variable_option = st.selectbox('Top 10 most of the games by :', (selectbox_options))
    total_data = df[variable_option].value_counts().head(10)
    chart_data = pd.DataFrame({variable_option: total_data.index, 'Count': total_data.values})
    chart_data = chart_data.sort_values(by='Count', ascending=True)
    st.bar_chart(chart_data.set_index(variable_option))

with a2:
    selectbox_options = [col for col in df.columns if col not in ['Name', 'Sales', 'Release']]
    variable_option = st.selectbox('Top 10 most of the sales by:', selectbox_options)
    total_data = df.groupby(variable_option)['Sales'].sum().nlargest(10)
    chart_data = pd.DataFrame({variable_option: total_data.index, 'Sales': total_data.values})
    chart_data = chart_data.sort_values(by='Sales', ascending=False)
    st.bar_chart(chart_data.set_index(variable_option), color="#ffa500")

df_reset = df.reset_index(drop=True)

st.dataframe(df_reset)
