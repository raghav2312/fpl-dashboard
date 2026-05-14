import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path


PROCESSED_PATH = Path("data/processed/manager_history.csv")


# Set the page configuration for the Streamlit app, including the title, icon, and layout. The page title is set to "FPL Dashboard", the page icon is set to a soccer emoji, and the layout is set to "wide" to utilize the full width of the browser window for displaying content.
st.set_page_config(
    page_title="FPL Dashboard", 
    page_icon=":soccer:",
    layout="wide")

st.title("Fantasy Premier League Season Dashboard")

df = pd.read_csv(PROCESSED_PATH)

#Top KPIs
latest = df.iloc[-1]


#Create four columns using Streamlit's st.columns function, which allows for the display of multiple metrics side by side. Each column will contain a metric related to the manager's performance in the Fantasy Premier League, such as total points, overall rank, team value, and money in the bank.
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Points", int(latest["total_points"]))
col2.metric("Overall Rank", int(latest["overall_rank"]))
col3.metric("Team Value", f"£{latest['team_value']/ 10:.1f}m")
col4.metric("Money in the Bank", f"£{latest['money_in_the_bank']/10:.1f}m")

st.divider()

#Rank Chart
st.subheader("Overall Rank Progression")


#Create a line chart using Plotly Express to visualize the overall rank progression of the manager across different gameweeks. The x-axis represents the gameweek number, while the y-axis represents the overall rank. Markers are added to each data point for better visibility, and the title of the chart is set to "Overall Rank by Gameweek". The y-axis is reversed to show better ranks (lower numbers) at the top of the chart.
points_fig = px.line(
    df, 
    x="gameweek", 
    y="overall_rank", 
    markers=True,
    title="Overall Rank by Gameweek",  
)



#Reverse the y-axis of the points_fig to show better ranks (lower numbers) at the top of the chart, which is a common convention for ranking visualizations. This is achieved by setting the autorange property of the y-axis to "reversed" using the update_yaxes method of the Plotly figure object.
points_fig.update_yaxes(autorange="reversed")

st.plotly_chart(points_fig, use_container_width=True)


#Rank Change Chart
st.subheader("Overall Rank Change by Gameweek")


#Create a bar chart using Plotly Express to visualize the overall rank change of the manager across different gameweeks. The x-axis represents the gameweek number, while the y-axis represents the rank change compared to the previous gameweek. The title of the chart is set to "Rank movement by Gameweek". Positive values indicate an improvement in rank, while negative values indicate a decline in rank.
rank_change_fig = px.bar(
    df,
    x="gameweek",
    y="rank_change",
    title="Rank movement by Gameweek"
)

st.plotly_chart(rank_change_fig, use_container_width=True)

#Raw table
st.subheader("Processed Gameweek Data")
st.dataframe(df)