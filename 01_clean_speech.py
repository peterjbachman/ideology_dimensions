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
speech_1 = df.loc[6002, "speech"]
speech_2 = df.loc[6003, "speech"]

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

# Embedding objects are numpy arrays where the dtype is np.float32

np.array([(1, 2), (3, 4)], dtype=np.float32)
