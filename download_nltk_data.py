import ssl
import nltk

ssl_context = ssl.create_default_context()
nltk.set_proxy('http://localhost:8080')
