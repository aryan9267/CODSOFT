import numpy as np
import pandas as pd

# Sample data: user ratings for items; 0 means no rating
data = {
    'Item1': [5, 4, 0, 2, 0],
    'Item2': [3, 0, 0, 5, 4],
    'Item3': [0, 0, 5, 4, 0],
    'Item4': [0, 3, 4, 0, 0],
    'Item5': [1, 0, 2, 4, 5]
}

# Create DataFrame with users as rows and items as columns
ratings = pd.DataFrame(data, index=['User1', 'User2', 'User3', 'User4', 'User5'])

# Function to find cosine similarity between two rating vectors
def similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot / (norm1 * norm2)

# Calculate similarities among users
user_sim = pd.DataFrame(index=ratings.index, columns=ratings.index)

for u1 in ratings.index:
    for u2 in ratings.index:
        user_sim.loc[u1, u2] = similarity(ratings.loc[u1], ratings.loc[u2])

user_sim = user_sim.astype(float)

# Make recommendations for a given user
def recommend(user_name, ratings_tbl, similarity_tbl, top_n=2):
    if user_name not in ratings_tbl.index:
        return f"No such user {user_name}"

    sim_scores = similarity_tbl.loc[user_name]
    weighted_scores = ratings_tbl.T.dot(sim_scores) / sim_scores.sum()
    already_rated = ratings_tbl.loc[user_name][ratings_tbl.loc[user_name] > 0].index

    recommendations = weighted_scores.drop(already_rated).sort_values(ascending=False)
    return recommendations.head(top_n)

# Show recommendations for User1
for user in ['User1', 'User2', 'User3', 'User4', 'User5']:
    result = recommend(user, ratings, user_sim)
    print(f"Items recommended for {user}:")
    print(result)
