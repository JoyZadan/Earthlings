import os
import re
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

# app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# app.secret_key = os.environ.get("SECRET_KEY")

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html", index_page=True)


@app.errorhandler(404)
def page_not_found(*args, **kwargs):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
