from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    boas_vindas = "LOGIN EFETUADO COM SUCESSO!"
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        if name == "wallem" and password == "102030":
            return redirect("/")
        else:
            error = "Login ou senha incorreto!"
    return render_template("login.html", error=error)