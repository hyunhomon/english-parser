import ssl
import nltk

ssl_context = ssl.create_default_context()
nltk.set_proxy('http://localhost:8080')

nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)

print(f"NLTK data is downloaded here: {nltk.data.path}")