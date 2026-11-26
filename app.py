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

if __name__ == "__main__":
    app.run(debug=True)
