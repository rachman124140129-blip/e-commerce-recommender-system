import pandas as pd
import os
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity

def load_artifacts():
    model = load_model('models/hybrid_model.h5')
    
    with open('models/user_encoder.pkl', 'rb') as f:
        user_enc = pickle.load(f)
        
    with open('models/item_encoder.pkl', 'rb') as f:
        item_enc = pickle.load(f)
        
    movies_df = pd.read_csv('data/processed/movies_clean.csv')
    visual_df = pd.read_csv('data/processed/visual_features.csv', index_col=0)
    
    return model, user_enc, item_enc, movies_df, visual_df

def get_hybrid_recommendations(user_id, top_n, model, user_enc, item_enc, movies_df, visual_df):
    user_idx = user_enc.transform([user_id])[0]
    all_items = np.arange(len(item_enc.classes_))
    user_array = np.full_like(all_items, user_idx)
    
    visual_features = visual_df.reindex(item_enc.classes_).values
    preds = model.predict([user_array, all_items, visual_features], verbose=0).flatten()
    
    top_indices = np.argsort(preds)[-top_n:][::-1]
    movie_ids = item_enc.inverse_transform(top_indices)
    
    recs = movies_df[movies_df['movieId'].isin(movie_ids)].copy()
    recs['pred_rating'] = preds[top_indices]
    
    return recs[['title', 'genres', 'poster_path', 'pred_rating']]

def get_similar_movies_by_title(title, top_n, movies_df, visual_df):
    idx = movies_df[movies_df['title'].str.contains(title, case=False)].index[0]
    query_vec = visual_df.iloc[idx].values.reshape(1, -1)
    sims = cosine_similarity(query_vec, visual_df.values).flatten()
    
    top_indices = np.argsort(sims)[-top_n-1:-1][::-1]
    
    recs = movies_df.iloc[top_indices].copy()
    recs['similarity'] = sims[top_indices]
    
    return recs[['title', 'genres', 'poster_path', 'similarity']]