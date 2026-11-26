from flask import Flask, request, send_from_directory

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
