from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def analyze_sentiment():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        if text:
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity
            
            if polarity > 0:
                result = "Positive Sentiment"
            elif polarity < 0:
                result = "Negative Sentiment"
            else:
                result = "Neutral Sentiment"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
