import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import Fore, init
import time
import sys

# 1. Initialize colorama
init(autoreset=True)

# 2. Load dataset
def load_data(file_path= "imdb_top_1000.csv"):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('').astype(str) + ' ' + df['Overview'].fillna('').astype(str) + ' ' + df['Actors'].fillna('').astype(str)