from models.sentiment_model import SentimentAnalysis

sentiment_analyzer = SentimentAnalysis()


def analyze_news_articles(articles):
    return [sentiment_analyzer.analyze_news(article) for article in articles]
