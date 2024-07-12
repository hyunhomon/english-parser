import nltk, ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

print(f"NLTK data is downloaded here: {nltk.data.path}")
