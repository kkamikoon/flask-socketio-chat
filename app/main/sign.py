import hashlib
from flask import (
    request,
    flash,
    redirect,
    render_template,
    url_for
)
from app.model import db, Users
from app.utils.security.auth import (
    signin_user,
    signout_user
)

from app.main import main


@main.route("/sign/in", methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form.get("email", default="", type=str)
        password = hashlib.sha3_512(request.form.get("password", type=str).encode()).hexdigest()

        # Query example 1
        user_info = db.session.query(
            Users.email,
            Users.name,
        ).filter(
            Users.email == email,
            Users.password == password
        ).one_or_none()

        if user_info == None:
            flash(message="No matched user information found.", category="error")
            return redirect(url_for(".signin"))
        else:
            signin_user(user_info)
            flash(message="Successfully signed in.", category="success")
            return redirect(url_for(".index"))

    return render_template(f"signin.html")


@main.route("/sign/up", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form.get("name", default="", type=str)
        email = request.form.get("email", default="", type=str)
        password = hashlib.sha3_512(request.form.get("password", type=str).encode()).hexdigest()
        confirm = hashlib.sha3_512(request.form.get("confirm", type=str).encode()).hexdigest()

        if confirm != password:
            return redirect(url_for(".signin"))
        
        # Query example 2 - Check unique user
        obj = Users.query.filter_by(email=email).one_or_none()
        if not obj:
            flash(message="User already exists.", category="error")
            return redirect(url_for(".signin"))

        user = Users(email=email, name=name, password=password)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            flash(message="Unknown error to sign up process.", category="error")
            db.session.rollback()
            return redirect(url_for(".signup"))
        else:
            db.session.commit()

        return redirect(url_for('.signin'))

    return render_template(f"signup.html")


@main.route("/sign/out", methods=['GET'])
def signout():
    signout_user()
    return redirect(url_for(".index"))
