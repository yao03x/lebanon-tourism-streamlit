import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Lebanon Tourism Explorer", layout="wide")
st.title("Lebanon Tourism Explorer")
st.write("Explore tourism activity across Lebanese towns using interactive visualizations.")
df = pd.read_csv("tourism_data.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())
st.sidebar.header("Filters")
min_index = int(df["Tourism Index"].min())
max_index = int(df["Tourism Index"].max())
tourism_range = st.sidebar.slider("Tourism Index Range", min_index, max_index, (min_index, max_index))
filtered_df = df[(df["Tourism Index"] >= tourism_range[0]) & (df["Tourism Index"] <= tourism_range[1])]
st.header("Tourism Index by Town")
fig1 = px.bar(filtered_df.head(20), x="Town", y="Tourism Index", title="Tourism Index Across Towns")
st.plotly_chart(fig1, use_container_width=True)
available_towns = sorted(filtered_df["Town"].dropna().unique())
selected_towns = st.sidebar.multiselect("Select Towns", available_towns, default=available_towns[:10])
final_df = filtered_df[filtered_df["Town"].isin(selected_towns)]
st.header("Restaurants vs. Tourism Index")
fig2 = px.scatter(final_df, x="Total number of restaurants", y="Tourism Index", hover_name="Town", title="Restaurants vs. Tourism Index")
st.plotly_chart(fig2, use_container_width=True)
st.header("Design Justifications")
st.subheader("1. Tourism Index Range Slider")
st.write("The Tourism Index slider helps users answer which towns fall within a specific level of tourism activity. A range slider was chosen because the Tourism Index is numerical and users can easily select a range of values instead of entering numbers manually. This interaction reduces clutter and focuses attention by displaying only the towns that are relevant to the selected tourism range.")
st.subheader("2. Town Multiselect")
st.write("The town multiselect helps users answer how specific towns compare after choosing a Tourism Index range. A multiselect was chosen instead of a single dropdown because users can compare several towns at the same time. It is linked to the Tourism Index slider because the available town options depend on the selected range. This supports drill-down analysis, reduces clutter, and focuses attention on relevant towns.")
