import fitz  # PyMuPDF
import re
import nltk

# Download required NLTK resources (runs only once; subsequent runs use cache)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def extract_text(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


stop = set(stopwords.words("english"))
lemm = WordNetLemmatizer()


def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    words = [lemm.lemmatize(w) for w in text.split() if w not in stop]
    return " ".join(words)


text = extract_text("./../data/aws_notes.pdf")
print(text)
print("CLEANED TEXT")
print(clean(text))
