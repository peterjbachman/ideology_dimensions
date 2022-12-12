"""
This Script cleans the floor speeches and prepares them for word embeddings.

Versions:
Python - 3.10.4
Pandas - 1.5.2
"""
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util

df_phil = pd.read_csv("data/universalism_populism_dimension.txt", sep="|")

# Define Model - Here is SBERT
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Create dimension matrix
dim = sum(
    model.encode(df_phil["universal"]) -
    model.encode(df_phil["populist"])) / 10

# Cosine Similarity. Here we go.
util.pytorch_cos_sim(test_2, dim).numpy()[0][0]

# Outline of the loop:
# - Load in the year
# - For each line on the year
# - Strip the periods and commas
# - Get the embedding and save it in a list with the speechid?
# - I can then use the speechid to tie each embedding with the respective
#   legislator.

# I also want to save a new dataset with only the speeches I keep, and their
# cleaned text just in case.

for j in range(82, 103):
    print(f"Starting on Session {j} of Congress")
    if j < 100:
        text_name = f"/Users/peter/Data/floor_speech/hein-bound/speeches_0{j}.txt"
    else:
        text_name = f"/Users/peter/Data/floor_speech/hein-bound/speeches_{j}.txt"

    # Load in text
    # Encoding issues are replaced with the hexidecimal form of the word
    df = pd.read_csv(text_name,
                     sep="|",
                     encoding="us-ascii",
                     encoding_errors='backslashreplace',
                     on_bad_lines="skip")

    # cleans dataset so that each of the speeches is longer than 30 words
    above_30 = df[df["speech"].str.split().str.len() > 30]

    # Clean out all periods and commas in the text since they are inconsistent.
    above_30["speech_cleaned"] = above_30["speech"].str.replace("\.|,",
                                                                "",
                                                                regex=True)

    print("Starting to find similarities between text")
    # Find embeddings for floor speeches
    embeddings = []
    df_sim = 0
    for i in range(above_30.shape[0]):
        embeddings.append([
            # Congress Session
            113,
            # speech id
            above_30.iloc[i, 0],
            # Similarity to dimension
            util.pytorch_cos_sim(model.encode(above_30.iloc[i, 2]),
                                 dim).numpy()[0][0]
        ])
    df_sim = pd.DataFrame(embeddings,
                          columns=["session", "speech_id", "similarity"])

    print("Saving as .csv")
    df_sim.to_csv(f"data/session_{j}_sim.csv")
