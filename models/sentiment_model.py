from transformers import pipeline


class SentimentAnalysis:
    def __init__(self):
        self.model = pipeline(
            "sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

    def analyze_news(self, text):
        return self.model(text)
