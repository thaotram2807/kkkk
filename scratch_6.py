import streamlit as st
import pandas as pd
import plotly.express as px
bar_graph = px.bar(
x = al_df["Date"],
y = al_df["Large Bags"],
title = "Bar Graph",
color=al_df["Large Bags"]
)
