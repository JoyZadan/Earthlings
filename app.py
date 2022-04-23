import os
# import re
# from datetime import datetime

# from bson.errors import InvalidId
# from cloudinary.exceptions import Error
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

# from helpers import upload_image

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

mongo = PyMongo(app)

animation_info = [
    {
        'title': 'water',
        'image': "static/assets/water.svg",
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'

    },
    {
        'title': 'plants',
        'image': 'static/assets/leaf.svg',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'

    },
    {
        'title': 'transport',
        'image': 'static/assets/bus.svg',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'
    },
    {
        'title': 'bag',
        'image': 'static/assets/bag.svg',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'

    },
    {
        'title': 'cycle',
        'image': 'static/assets/bicycle.svg',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'

    },
    {
        'title': 'solar',
        'image': 'static/assets/sun.svg',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'

    },
    {
        'title': 'heat',
        'image': 'static/assets/thermometer.svg',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'

    },
    {
        'title': 'energy',
        'image': 'static/assets/electricity.svg',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In enim velit, imperdiet et sapien ultricies, cursus interdum justo. Vivamus consequat, ligula quis faucibus ultricies, sapien sem aliquet dolor, sed blandit nunc turpis nec nisl. Sed consectetur malesuada sem, sed eleifend nulla mattis quis. Ut sollicitudin auctor dolor eget egestas. Sed in dolor eget massa volutpat cursus sed eget est. Maecenas euismod, purus ac efficitur euismod, ipsum quam vehicula metus, sit amet ullamcorper orci orci in leo. Maecenas porttitor fringilla mi, vitae laoreet purus. Suspendisse ultrices eros pharetra, lacinia erat sit amet, sollicitudin augue. Cras iaculis aliquet massa, at cursus nisl elementum eu. In sed metus pharetra justo dictum elementum. Etiam pulvinar augue in mauris pellentesque bibendum. Maecenas non venenatis felis, non malesuada urna.'
    }
]

@app.route("/")
def index():
    return render_template("index.html", index_page=True, animation_info=animation_info)



# ==========handle login logout register======================================
@app.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        return redirect(url_for('profile'))
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        validate_password = True if request.form.get("password") == request.form.get("password2") else flash("Passwords not matching")
        if validate_password:
            register_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register_user)
            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("index"))
        else:
            return redirect((url_for('register')))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for('profile'))
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("index"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    if "user" in session:
        # remove user from session cookie
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("index"))

    return redirect(url_for('index'))


class Error(Exception):  # Class from cloudinary used here temporary
    pass


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    """
    User profile check if user exists, if not redirects to home page
    """
    # grab the session user's username from db
    if request.method == "POST":
        pass
    try:
        mongo.db.users.find_one({
            "username": session["user"]
        })["username"]
    except Error:
        return redirect(url_for("login"))
    if "user" in session:
        # user_history = list(mongo.db.user_profile.find({"username": {"$eq": session["user"]}}))
        # return render_template("profile.html", user_history=user_history)
        return render_template("profile.html")
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(*args, **kwargs):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/categories")
def categories():
    if "user" in session:
        categories = list(mongo.db.categories.find())
        return render_template("categories.html",
                            categories=categories)
    else:
        return render_template('404.html'), 404


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    ''' 
    Add a category
    '''
    if "user" in session:
        if request.method =="POST":
            category_name = request.form.get("category_name")
            category_description = request.form.get("category_description")
            category = {
                "name" : category_name,
                "description" : category_description
            }
            mongo.db.categories.insert_one(category)
            return redirect(url_for("categories"))
        return render_template("add_category.html")
    else:
        return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
