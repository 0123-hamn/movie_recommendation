import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🎬 Movie Recommender System")

# Fetch movie list
movies = requests.get(f"{API_URL}/movies").json()["movies"]

selected_movie = st.selectbox(
    "Select a movie",
    movies
)

if st.button("Recommend"):

    response = requests.get(
        f"{API_URL}/recommend",
        params={"movie": selected_movie}
    )

    recs = response.json()["recommendations"]

    st.subheader("Recommended Movies")

    for movie in recs:
        st.write(movie)