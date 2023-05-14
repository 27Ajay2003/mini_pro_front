import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict
import numpy as np

# nltk.download('stopwords')
# nltk.download('punkt')

def get_top_keywords(document, num_keywords=5):
    # Tokenize the document into sentences and words
    sentences = sent_tokenize(document)
    words = word_tokenize(document)

    # Remove stopwords and punctuation marks
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    words = [word.lower() for word in words if word.lower() not in stop_words and tokenizer.tokenize(word)]

    # Build the graph and compute the PageRank scores
    graph = defaultdict(list)
    for i, word_i in enumerate(words):
        for j, word_j in enumerate(words):
            if i != j:
                if word_j not in graph[word_i]:
                    graph[word_i].append(word_j)
                    graph[word_j].append(word_i)

    pagerank_scores = np.zeros(len(words))
    damping_factor = 0.85
    num_iterations = 50

    for i in range(num_iterations):
        for j, word in enumerate(words):
            incoming_scores = [pagerank_scores[k] / len(graph[words[k]]) for k in range(len(words)) if word in graph[words[k]]]
            pagerank_scores[j] = (1 - damping_factor) + damping_factor * sum(incoming_scores)

    # Get the top N keywords
    top_indices = np.argsort(pagerank_scores)[::-1][:num_keywords]
    keywords = [words[index] for index in top_indices]

    # Return the keywords as a string separated by spaces
    return ' '.join(keywords)