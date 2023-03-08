import hashlib
from flask import current_app as app
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
            return redirect(url_for(".signin"))
        else:
            signin_user(user_info)
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
        if obj != None:
            print(f"No unique!!!!!!!!!!!!!")
            return redirect(url_for(".signin"))

        user = Users(email=email, name=name, password=password)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(f"[-] failed to add user {e}")
            db.session.rollback()
            return redirect(url_for(".signup"))
        else:
            db.session.commit()

        print("GOOOOD", user)
        return redirect(url_for('.signin'))


    return render_template(f"signup.html")


@main.route("/sign/out", methods=['GET'])
def signout():
    signout_user()
    return render_template(f"index.html")