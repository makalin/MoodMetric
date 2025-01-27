from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from transformers import pipeline

# Download NLTK data (only needed for the first time)
nltk.download('vader_lexicon')

class MoodMetric:
    def __init__(self):
        # Initialize sentiment analyzers
        self.sia = SentimentIntensityAnalyzer()
        self.emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    def analyze_sentiment(self, text):
        # Analyze sentiment using TextBlob
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity

        # Analyze sentiment using NLTK's Vader
        sentiment_scores = self.sia.polarity_scores(text)

        # Determine sentiment based on polarity
        if sentiment_polarity > 0:
            sentiment = "Positive"
        elif sentiment_polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {
            "text": text,
            "sentiment": sentiment,
            "polarity": sentiment_polarity,
            "vader_scores": sentiment_scores
        }

    def analyze_emotion(self, text):
        # Analyze emotion using Hugging Face model
        emotion_result = self.emotion_analyzer(text)
        emotion = emotion_result[0]['label']
        emotion_score = emotion_result[0]['score']

        return {
            "text": text,
            "emotion": emotion,
            "emotion_score": emotion_score
        }

    def full_analysis(self, text):
        sentiment_result = self.analyze_sentiment(text)
        emotion_result = self.analyze_emotion(text)

        return {
            "sentiment_analysis": sentiment_result,
            "emotion_analysis": emotion_result
        }

# Example usage
if __name__ == "__main__":
    analyzer = MoodMetric()
    text = "I absolutely love this product! It's fantastic and works perfectly."

    # Full analysis
    analysis = analyzer.full_analysis(text)
    print("Sentiment Analysis:", analysis["sentiment_analysis"])
    print("Emotion Analysis:", analysis["emotion_analysis"])