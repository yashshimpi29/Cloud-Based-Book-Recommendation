import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

# Current directory for Flask app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(APP_ROOT, 'top90percentile_books.xlsx')

q_books = pd.read_excel(file_path)

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(q_books['description'].values.astype('U'))

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix)

indices = pd.Series(q_books.index, index=q_books['Book_detail']).drop_duplicates()

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    book_result = q_books.iloc[movie_indices]
    r_books_1 = book_result.to_json(orient="records")
    r_books = json.loads(r_books_1)

    # Return the top 10 most similar movies
    return r_books
