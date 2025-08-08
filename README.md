## 🎬 Movie Recommendation System using Machine Learning  

This project recommends movies 🍿🎥 based on content similarity, using **cosine similarity** over processed movie metadata. It integrates **Streamlit** for an interactive UI and uses **TMDB API** to fetch posters 🎭.  

### ✨ Features  
- 🔍 Content-based movie recommendations  
- 🎭 Metadata preprocessing: genres, keywords, cast, and crew  
- 🧠 NLP with stemming using NLTK for better similarity matching  
- 🖼️ Fetches movie posters from TMDB API  
- ⚡ Interactive and user-friendly interface with Streamlit  
- 📦 Pickle-based model storage for quick loading  

### 🛠️ Technologies Used  
- 🐍 Python  
- 📊 Pandas, NumPy  
- 📜 NLTK (Porter Stemmer)  
- 🤖 Scikit-learn (cosine similarity)  
- 🌐 Requests (TMDB API)  
- 🎨 Streamlit for frontend UI  

### ⚙️ How it Works  
1. 📥 Load and merge TMDB movie and credits datasets  
2. 🔍 Extract and clean metadata (genres, keywords, cast, crew)  
3. 🧠 Process text with stemming to unify word forms  
4. 📊 Convert tags to vectors and compute cosine similarity  
5. 🎯 Recommend top 5 similar movies for a given title  
6. 🖼️ Fetch posters for recommendations using TMDB API  
