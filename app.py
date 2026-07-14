from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
@app.route("/predict", methods=["POST"])
def predict():
    return "AI Caption will appear here."