from flask import Flask, request

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return "Employee Management Portal"

if __name__ == "__main__":
    app.run(debug=True)
