import easyocr

class ImageRecognizer:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])
    
    def recognize(self, path):
        result = self.reader.readtext(path)

        extracted_text = ""
        for (_, text, _) in result:
            extracted_text += text
        
        return extracted_text
