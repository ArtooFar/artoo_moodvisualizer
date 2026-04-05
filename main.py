from pathlib import Path

import plotly.express as px
import streamlit as st
import nltk

import backend as be


nltk.download("vader_lexicon", quiet=True)

st.set_page_config(page_title="Mood Visualizer", layout="centered")
st.title("Mood Visualizer")
st.caption("Track positivity and negativity trends from diary entries using NLTK sentiment analysis.")

DIARY_DIR = Path(__file__).parent / "diary"
files_and_content = be.get_files_and_content(DIARY_DIR)

if not files_and_content:
    st.warning("No diary entries found in the 'diary' folder.")
    st.stop()

st.subheader("Positivity")
pdates, pcontent = be.get_positivity_and_date_list(files_and_content)
st.plotly_chart(
    px.line(x=pdates, y=pcontent, labels={"x": "Date", "y": "Positivity"}),
    width='stretch',
)

st.subheader("Negativity")
ndates, ncontent = be.get_negativity_and_date_list(files_and_content)
st.plotly_chart(
    px.line(x=ndates, y=ncontent, labels={"x": "Date", "y": "Negativity"}),
    width='stretch',
)
