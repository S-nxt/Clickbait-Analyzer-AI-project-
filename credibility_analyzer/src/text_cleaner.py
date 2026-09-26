import re
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Cleans raw article text by lowercasing, removing non-alphabetic
    characters, and stripping NLTK english stopwords.
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = [word for word in text.split() if word not in stop_words]
    return " ".join(words)