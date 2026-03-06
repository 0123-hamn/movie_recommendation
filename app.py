from fastapi import FastAPI
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# load files
movies = pickle.load(open("df.pkl","rb"))
indices = pickle.load(open("indices.pkl","rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl","rb"))

movie_list = movies['title'].values


@app.get("/")
def home():
    return {"message":"Movie Recommendation API running"}


@app.get("/movies")
def get_movies():
    return {"movies": list(movie_list)}


@app.get("/recommend")
def recommend(movie:str,n:int=5):

    if movie not in indices:
        return {"recommendations":[]}

    idx = indices[movie]

    sim_score = cosine_similarity(tfidf_matrix[idx],tfidf_matrix).flatten()
    similar_idx = sim_score.argsort()[::-1][1:n+1]

    recs = movies['title'].iloc[similar_idx].tolist()

    return {"recommendations": recs}