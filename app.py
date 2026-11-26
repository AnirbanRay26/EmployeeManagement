from flask import Flask, request, send_from_directory

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/register", methods=["POST"])
def register_employee():
    name = request.form.get("name")
    email = request.form.get("email")

    employee = {
        "name": name,
        "email": email
    }

    employees.append(employee)

    return "Employee registered successfully!"

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
