from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    text_lower = text.lower()

    # Custom neutral words
    neutral_words = ["okay", "ok", "fine", "average"]

    if any(word in text_lower for word in neutral_words):
        return "Neutral 😐"
    elif score > 0.2:
        return "Positive 😊"
    elif score < -0.2:
        return "Negative 😞"
    else:
        return "Neutral 😐"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        user_text = request.form['text']
        result = get_sentiment(user_text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)