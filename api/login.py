from flask import Blueprint, render_template, request, redirect, session

auth = Blueprint("auth", __name__)

# 🔐 Identifiants par défaut (à personnaliser)
UTILISATEUR = {
    "username": "admin",
    "password": "secret"  # change ce mot de passe !
}

@auth.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")
        if user == UTILISATEUR["username"] and pwd == UTILISATEUR["password"]:
            session["user"] = user
            return redirect("/dashboard")
        else:
            error = "Identifiants incorrects"
    return render_template("login.html", error=error)

@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/login")