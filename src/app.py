import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path
from charts import create_rank_chart, create_points_chart, create_rank_change_chart, create_bench_points_chart


PROCESSED_PATH = Path("data/processed/manager_history.csv")


# Set the page configuration for the Streamlit app, including the title, icon, and layout. The page title is set to "FPL Dashboard", the page icon is set to a soccer emoji, and the layout is set to "wide" to utilize the full width of the browser window for displaying content.
st.set_page_config(
    page_title="FPL Dashboard", 
    page_icon=":soccer:",
    layout="wide")

st.title("Fantasy Premier League Season Dashboard")
st.caption("Personal FPL performance tracker")


df = pd.read_csv(PROCESSED_PATH)

#Sidebar filter
st.sidebar.header("Filters")

min_gw = int(df["gameweek"].min())
max_gw = int(df["gameweek"].max())

selected_gws = st.sidebar.slider(
    "Select Gameweek Range",
    min_value=min_gw,
    max_value=max_gw,
    value=(min_gw, max_gw)
)

filtered_df = df[(df["gameweek"] >= selected_gws[0]) & (df["gameweek"] <= selected_gws[1])]

#KPI Calculations
latest = filtered_df.iloc[-1]


#assign the row with the maximum "gw_points" value to the variable "best_gw" and the row with the minimum "gw_points" value to the variable "worst_gw". Similarly, assign the row with the maximum "rank_change" value to the variable "biggest_rank_gain" and the row with the minimum "rank_change" value to the variable "biggest_rank_drop". These variables will be used later in the code to display key performance indicators (KPIs) related to the manager's performance in the Fantasy Premier League.
best_gw = filtered_df.loc[filtered_df["gw_points"].idxmax()]
worst_gw = filtered_df.loc[filtered_df["gw_points"].idxmin()]
biggest_rank_gain = filtered_df.loc[filtered_df["rank_change"].idxmax()]
biggest_rank_drop = filtered_df.loc[filtered_df["rank_change"].idxmin()]


avg_points = filtered_df["gw_points"].mean()
total_bench_points = filtered_df["bench_points"].sum()
total_transfer_cost = filtered_df["transfer_cost"].sum()



#Top KPI Cards
st.subheader("Season Summary")

#Create four columns using Streamlit's st.columns function, which allows for the display of multiple metrics side by side. Each column will contain a metric related to the manager's performance in the Fantasy Premier League, such as total points, overall rank, team value, and money in the bank.
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Points", int(latest["total_points"]))
col2.metric("Overall Rank", int(latest["overall_rank"]))
col3.metric("Team Value", f"£{latest['team_value']/ 10:.1f}m")
col4.metric("Money in the Bank", f"£{latest['money_in_the_bank']/10:.1f}m")



#Create another set of four columns to display additional metrics related to the manager's performance, such as the best gameweek points, worst gameweek points, total bench points lost, and total transfer cost. Each column will contain a metric with a title and a value, providing insights into the manager's performance across different gameweeks.
col5, col6, col7, col8 = st.columns(4)
col5.metric("Best GW", f'GW{int(best_gw['gameweek'])}')
col6.metric("Worst GW", f'GW{int(worst_gw['gameweek'])}')
col7.metric("Bench Points Lost", int(total_bench_points))
col8.metric("Total Transfer Cost", int(total_transfer_cost))

st.divider()

#Rank Chart
st.subheader("Overall Rank Progression")


#Create a line chart using Plotly Express to visualize the overall rank progression of the manager across different gameweeks. The x-axis represents the gameweek number, while the y-axis represents the overall rank. Markers are added to each data point for better visibility, and the title of the chart is set to "Overall Rank by Gameweek". The y-axis is reversed to show better ranks (lower numbers) at the top of the chart.
#Reverse the y-axis of the rank_fig to show better ranks (lower numbers) at the top of the chart, which is a common convention for ranking visualizations. This is achieved by setting the autorange property of the y-axis to "reversed" using the update_yaxes method of the Plotly figure object.
st.plotly_chart(create_rank_chart(filtered_df), use_container_width=True)




#Points Chart
st.subheader("Gameweek Points")

#Create a bar chart using Plotly Express to visualize the points scored by the manager in each gameweek. The x-axis represents the gameweek number, while the y-axis represents the points scored in that gameweek. The title of the chart is set to "Points by gameweek". Each bar in the chart corresponds to the points scored in a specific gameweek, allowing for easy comparison across different gameweeks.
st.plotly_chart(create_points_chart(filtered_df), use_container_width=True)




#Rank Change Chart
st.subheader("Rank Movement")

#Create a bar chart using Plotly Express to visualize the overall rank change of the manager across different gameweeks. The x-axis represents the gameweek number, while the y-axis represents the rank change compared to the previous gameweek. The title of the chart is set to "Rank movement by Gameweek". Positive values indicate an improvement in rank, while negative values indicate a decline in rank.
st.plotly_chart(create_rank_change_chart(filtered_df), use_container_width=True)



#Create a bar chart using Plotly Express to visualize the bench points lost by the manager in each gameweek. The x-axis represents the gameweek number, while the y-axis represents the bench points lost in that gameweek. The title of the chart is set to "Bench Points Lost by Gameweek". Each bar in the chart corresponds to the bench points lost in a specific gameweek, allowing for easy comparison across different gameweeks.
st.subheader("Bench Points Lost")
st.plotly_chart(create_bench_points_chart(filtered_df), use_container_width=True)


#Data table
st.subheader("Processed Gameweek Data")
st.dataframe(df)