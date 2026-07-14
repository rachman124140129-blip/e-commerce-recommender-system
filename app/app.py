import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import sys
sys.path.append('.')

from src.utils.helpers import load_artifacts, get_hybrid_recommendations, get_similar_movies_by_title

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender dengan Computer Vision")
st.markdown("Rekomendasi film berdasarkan preferensi pengguna dan kemiripan visual poster.")

@st.cache_resource
def load_resources():
    return load_artifacts()

model, user_enc, item_enc, movies_df, visual_df = load_resources()

st.sidebar.header("Pilih Metode Rekomendasi")
mode = st.sidebar.radio("Mode", ("Berdasarkan User ID", "Berdasarkan Judul Film"))

if mode == "Berdasarkan User ID":
    user_id = st.sidebar.number_input("Masukkan User ID", min_value=1, max_value=len(user_enc.classes_), value=1)
    top_n = st.sidebar.slider("Jumlah rekomendasi", 5, 20, 10)
    if st.sidebar.button("Rekomendasikan"):
        recs = get_hybrid_recommendations(user_id, top_n, model, user_enc, item_enc, movies_df, visual_df)
        display_recommendations(recs)
else:
    movie_title = st.sidebar.text_input("Ketik judul film", "Toy Story")
    top_n = st.sidebar.slider("Jumlah rekomendasi", 5, 20, 10)
    if st.sidebar.button("Cari Film Serupa"):
        recs = get_similar_movies_by_title(movie_title, top_n, movies_df, visual_df)
        display_recommendations(recs)
        
def display_recommendations(recs):
    cols = st.columns(5)
    for i, (_, row) in enumerate(recs.iterrows()):
        col = cols[i % 5]
        if 'poster_path' in row and pd.notna(row['poster_path']):
            poster_url = "https://image.tmdb.org/t/p/w154" + row['poster_path']
            try:
                response = requests.get(poster_url)
                img = Image.open(BytesIO(response.content))
                col.image(img, width=130)
            except:
                col.image("https://via.placeholder.com/130x195.png?text=No+Poster", width=130)
        else:
            col.image("https://via.placeholder.com/130x195.png?text=No+Poster", width=130)
        col.markdown(f"**{row['title']}**")
        if 'pred_rating' in row:
            col.caption(f"⭐ {row['pred_rating']:.1f}")
        elif 'similarity' in row:
            col.caption(f"Similar: {row['similarity']:.2f}")