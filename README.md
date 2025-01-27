# MoodMetric - Sentiment and Emotion Analysis Tool

MoodMetric is a Python-based tool for analyzing the sentiment and emotion of text. It leverages multiple libraries and models, including TextBlob, NLTK's Vader, and a Hugging Face emotion classification model, to provide comprehensive sentiment and emotion analysis.

## Features

- **Sentiment Analysis**: Determines whether the text is positive, negative, or neutral using TextBlob and NLTK's Vader.
- **Emotion Analysis**: Identifies the emotion expressed in the text using a pre-trained Hugging Face model.
- **Full Analysis**: Combines both sentiment and emotion analysis into a single output.

## Installation

To use MoodMetric, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/moodmetric.git
   cd moodmetric
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the dependencies manually:
   ```bash
   pip install textblob nltk transformers
   ```

3. **Download NLTK data** (required for the first time):
   ```python
   python -c "import nltk; nltk.download('vader_lexicon')"
   ```

## Usage

You can use MoodMetric to analyze the sentiment and emotion of any text. Here's an example of how to use it:

```python
from mm import MoodMetric

# Initialize the analyzer
analyzer = MoodMetric()

# Analyze a sample text
text = "I absolutely love this product! It's fantastic and works perfectly."
analysis = analyzer.full_analysis(text)

# Print the results
print("Sentiment Analysis:", analysis["sentiment_analysis"])
print("Emotion Analysis:", analysis["emotion_analysis"])
```

### Output Example

```plaintext
Sentiment Analysis: {
    'text': "I absolutely love this product! It's fantastic and works perfectly.",
    'sentiment': 'Positive',
    'polarity': 0.8,
    'vader_scores': {
        'neg': 0.0,
        'neu': 0.18,
        'pos': 0.82,
        'compound': 0.875
    }
}

Emotion Analysis: {
    'text': "I absolutely love this product! It's fantastic and works perfectly.",
    'emotion': 'joy',
    'emotion_score': 0.98
}
```

## Dependencies

- [TextBlob](https://textblob.readthedocs.io/): For basic sentiment analysis.
- [NLTK](https://www.nltk.org/): For Vader sentiment analysis.
- [Transformers](https://huggingface.co/transformers/): For emotion analysis using Hugging Face models.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
