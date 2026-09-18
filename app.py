from flask import Flask, render_template, request
import re

app = Flask(__name__)

def summarize(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)

    if len(sentences) <= 2:
        return text

    return " ".join(sentences[:2])

@app.route("/", methods=["GET", "POST"])
def home():

    summary = None

    if request.method == "POST":
        text = request.form["text"]
        summary = summarize(text)

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
