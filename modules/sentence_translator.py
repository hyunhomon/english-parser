from googletrans import Translator

class SentenceTranslator():
    def __init__(self):
        self.translator = Translator()

    def translate(self, text):
        try:
            translated_text = self.translator.translate(text, dest='ko')
            return translated_text.text
        except Exception as e:
            return f'Error: {e}'
