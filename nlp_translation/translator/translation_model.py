from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-en-hi"
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = self.model.generate(**inputs)
        translated_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return translated_text
