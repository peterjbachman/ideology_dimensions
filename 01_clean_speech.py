"""
This Script cleans the floor speeches and prepares them for word embeddings.

Versions:
Python - 3.11.0
Pandas - 1.5.2
"""
import pandas as pd
from nltk import tokenize
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('bert-base-cased')

# Load in text
# Encoding issues are replaced with the hexidecimal form of the word
df = pd.read_csv("/Users/peter/Data/floor_speech/hein-daily/speeches_113.txt",
                 sep="|",
                 encoding="us-ascii",
                 encoding_errors='backslashreplace')

# Gets the speech
df.loc[6002, "speech"]

# Tokenizes one line of the dataset
tokenizer(df.loc[6002, "speech"])

# Okay the OCR maybe has issues with punctuation. Should I just remove
# punctuation then?
tokenize.sent_tokenize(df.loc[6002, "speech"])