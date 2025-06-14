import streamlit as st
import pickle
import pandas as pd
import requests


movie_list_df = pickle.load(open('movie.pkl', 'rb'))
similar = pickle.load(open('similar.pkl', 'rb'))

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US',
            timeout=5
        )
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    movie_idx = movie_list_df[movie_list_df['title'] == movie].index[0]
    distances = similar[movie_idx]
    movie_ = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    m = []
    mm=[]
    for i in movie_:
        mov_id=movie_list_df.iloc[i[0]].id
        mm.append(fetch_poster(mov_id))
        m.append(movie_list_df.iloc[i[0]].title)
    return m,mm

# Now extract titles only for display
movie_titles = movie_list_df['title'].values

st.title('Movie Recommendation System by SAMARTH')
movie_name = st.selectbox(
    'Welcome to the movie recommendation tab',
    movie_titles
)

if st.button('Recommend'):
    names, posters = recommend(movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

import streamlit as st

import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=cover,format=auto,quality=85,width=1920/keyart/G5PHNMW59-backdrop_wide");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

