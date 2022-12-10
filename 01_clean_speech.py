"""
This Script cleans the floor speeches and prepares them for word embeddings.

Versions:
Python - 3.11.0
Pandas - 1.5.2
"""
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Load in text
# Encoding issues are replaced with the hexidecimal form of the word
df = pd.read_csv("/Users/peter/Data/floor_speech/hein-daily/speeches_113.txt",
                 sep="|",
                 encoding="us-ascii",
                 encoding_errors='backslashreplace')

# Define Model - Here is SBERT
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Gets the speech
speech_1 = df.loc[6000, "speech"]
speech_2 = df.loc[6003, "speech"]

len(speech_1.split())

# Remove punctuation, since OCR is not good at identifying periods and commas
# accurately
speech_cleaned_1 = speech_1.replace(".", "")
speech_cleaned_1 = speech_cleaned_1.replace(",", "")

speech_cleaned_2 = speech_2.replace(".", "")
speech_cleaned_2 = speech_cleaned_2.replace(",", "")

# Convert sentences to sentence-level embeddings
test_1 = model.encode(speech_cleaned_1)
test_2 = model.encode(speech_cleaned_2)

# Cosine Similarity. Here we go.
util.pytorch_cos_sim(test_1, test_2).numpy()[0][0]

# I need to fine tune the model I think. But on how much of the data?
# What is the lower cutoff for sentence length where I decide it's a formality?
# I'm thinking 30 words here will be a good cutoff.

# Embedding objects are numpy arrays where the dtype is np.float32

np.array([(1, 2), (3, 4)], dtype=np.float32)

# Outline of the loop:
# - Load in the year
# - For each line on the year
# - Strip the periods and commas
# - Get the embedding and save it in a list with the speechid?
# - I can then use the speechid to tie each embedding with the respective
#   legislator.

# I also want to save a new dataset with only the speeches I keep, and their
# cleaned text just in case.

# cleans dataset so that each of the speeches is longer than 30 words
above_30 = df[df["speech"].str.split().str.len() > 30]

# Clean out all periods and commas in the text since they are inconsistent.
above_30["speech_cleaned"] = above_30["speech"].str.replace("\.|,", "")

embeddings = []

for i in range(above_30.shape[0]):
    embeddings.append([
        # Congress Session
        113,
        # speech id
        above_30.iloc[i, 0],
        # embedding for the speech
        model.encode(above_30.iloc[i, 2])
    ])

embeddings[65004]