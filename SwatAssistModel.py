import random
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Download necessary NLTK resources
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load the data
try:
    df = pd.read_excel('SwatAssist.xlsx')
except FileNotFoundError:
    print("Error: Could not find input file.")
    exit()

# Extract questions and answers from the dataset
questions = df['question'].tolist()
answers = df['answer'].tolist()

# Preprocess the data
tokens = []
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(word):
    """Map POS tag to first character used by WordNetLemmatizer"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


for question in questions:
    # Tokenize the question
    token = word_tokenize(question.lower())
    # Filter out stop words
    filtered_token = [word for word in token if word not in stop_words]
    # Lemmatize the words using WordNetLemmatizer
    lemmatized_token = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(word)) for word in filtered_token]
    tokens.append(lemmatized_token)

# Create a vectorizer object and transform the tokens into vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([" ".join(tokens_in_question) for tokens_in_question in tokens])

# Define the threshold for the cosine similarity
SIMILARITY_THRESHOLD = 0.4

# Define the default answer
DEFAULT_ANSWER = "Thank you for escalating this question. We have forwarded your question to our Technical Team for " \
                 "further research. Once we have an update available we will notify you"

# Define the paths to the sentiment analysis models
ANALYZER_PATH = os.path.join(os.getcwd(), 'sentiment', 'vader_lexicon.zip')
TB_POLARITY_PATH = os.path.join(os.getcwd(), 'sentiment', 'tb_polarity.pickle')


# Define a function to find the most similar question in the dataset
def find_most_similar_question(question):
    # If the question is not a greeting, find the most similar question
    # Preprocess the question
    token = word_tokenize(question.lower())
    filtered_token = [word for word in token if word not in stop_words]
    lemmatized_token = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in filtered_token]
    # Transform the question into a vector
    vector = vectorizer.transform([" ".join(lemmatized_token)])
    # Calculate the cosine similarity between the question and the dataset
    similarity_scores = cosine_similarity(vector, vectors)[0]
    # Find the most similar question and its index in the dataset
    most_similar_question_index = similarity_scores.argmax()
    most_similar_question = questions[most_similar_question_index]
    # If the similarity score is above the threshold, return the corresponding answer
    if similarity_scores[most_similar_question_index] >= SIMILARITY_THRESHOLD:
        answer = answers[most_similar_question_index]
    else:
        answer = DEFAULT_ANSWER
    return answer
