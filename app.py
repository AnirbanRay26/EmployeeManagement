from flask import Flask, request, send_from_directory

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/search")
def search_employee():
    name = request.args.get("name")

    results = [
        emp for emp in employees
        if name and name.lower() in emp["name"].lower()
    ]

    return str(results)

if __name__ == "__main__":
    app.run(debug=True)
