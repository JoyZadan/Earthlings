import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

mongo = PyMongo(app)

# animation_info = [
#     {
#         'title': 'Water',
#         'image': "static/assets/water.svg",
#         'content': '''Contaminated water and poor sanitation are linked to transmission of diseases such as cholera, diarrhoea, dysentery, hepatitis A, typhoid and polio. Absent, inadequate, or inappropriately managed water and sanitation services expose individuals to preventable health risks. This is particularly the case in health care facilities where both patients and staff are placed at additional risk of infection and disease when water, sanitation and hygiene services are lacking. Globally, 15% of patients develop an infection during a hospital stay, with the proportion much greater in low-income countries.
#
#         Inadequate management of urban, industrial and agricultural wastewater means the drinking-water of hundreds of millions of people is dangerously contaminated or chemically polluted. Natural presence of chemicals, particularly in groundwater, can also be of health significance, including arsenic and fluoride, while other chemicals, such as lead, may be elevated in drinking-water as a result of leaching from water supply components in contact with drinking-water.
#         ''',
#
#     },
#     {
#         'title': 'Plants',
#         'image': 'static/assets/leaf.svg',
#         'content': '''If people are good at something, then it is building up excess carbon dioxide in the atmosphere. Harmful CO2 contributes to climate change, the biggest current problem the world has to deal with. Trees, however, help fight it. They absorb CO2 removing it from the air and storing it while releasing oxygen. Annually, an acre of trees absorbs the amount of carbon dioxide equal to driving your car 26 000 miles. Trees are our main survival tools; only one tree can produce enough oxygen for four people.
#
#                     Have you ever felt that feeling of „cleaner air“ in the woods or by the seaside? Well, you were right because it is well known that trees do purify the air. They absorb pollutant gases such as nitrogen oxides, ozone, ammonia, sulfur dioxide. Trees also absorb odors and act as a filter as little particulates get trapped in leaves. A mature acre of trees can yearly provide oxygen for 18 people.'''
#     },
#     {
#         'title': 'Transport',
#         'image': 'static/assets/bus.svg',
#         'content': '''Public Transportation has the ability to drastically reduce pollution when capitalised by commuters. The Center for Climate and Energy Solutions (C2ES) state that “Communities with strong public transportation can reduce the nation’s [United States] carbon emissions by 37 million metric tons yearly.”
#
#                     And according to the U.S. Environmental Protection Agency, 41% of Greenhouse Gases caused by transport were emitted by cars in 2018. '''
#     },
#     {
#         'title': 'Bag',
#         'image': 'static/assets/bag.svg',
#         'content': '''The Center for Biological Diversity reports that harm to at least 267 different species has been attributed to plastic pollution in the oceans.
#
#                     Plastic bags alone kill up to 100,000 marine animals every year. One species that is especially hard-hit is the leatherback sea turtle, which often confuses plastic bags for the jellyfish they like to eat. 1 of every 3 leatherbacks is found with plastic in its stomach, according to the Centers for Biological Diversity.
#
#                     Residents of the United States use nearly one single-use plastic bag per person per day. Let’s put that into perspective, thanks to the National Geographic Society: Danish shoppers use only about four plastic bags per year.
#
#                     The Earth Day Network states that only about 1% of the 4 trillion plastic bags used worldwide annually are recycled, and residents of the United States throw away up to 100 billion plastic bags every year.
#
#                     A plastic bag takes up to 500 years to degrade in a landfill. According to the Earth Day Network, as plastic bags break down, they absorb toxins which can then be released into the wind, water, or ground.'''
#     },
#     {
#         'title': 'Cycle',
#         'image': 'static/assets/bicycle.svg',
#         'content': '''We already know that cycling reduces the risk of heart disease and cancer – largely because cycling is great exercise. But did you know that cycling is also good for weight loss (which offers the roundabout benefit that when you weigh less, cycling becomes easier)?
#
#         Cycling makes our body release feel good hormones. When we cycle, we feel better – we can’t get away from it. When hormones like serotonin, dopamine and endorphins are released, stress and anxiety is reduced. Finding ways to be happier more often and for longer is especially important now, as an uncertain economic climate is taking its toll on employee morale across the UK.'''
#     },
#     {
#         'title': 'Solar',
#         'image': 'static/assets/sun.svg',
#         'content': '''Did you know that the energy sun provides to the earth for one hour could meet the global energy needs for one year? Undoubtedly, the sun is a powerful energy source, and even though we are not able but to collect a fraction of this energy, yet harnessing this power by installing solar panels can make a significant difference to the planet.
#
#         While it has been widely criticised for being expensive or inefficient, solar energy has now proved to be extremely beneficial - not only for the environment but also for the private economy.
#
#         Thanks to available solar panel grants, as well as, the increasingly competitive prices in the market, solar energy has become the main source of energy for more and more families. The technology has been drastically improved the last years and has been complemented by solar battery storage systems, turning solar into a significantly more efficient source of clean energy.'''
#     },
#     {
#         'title': 'Heat',
#         'image': 'static/assets/thermometer.svg',
#         'content': '''Reducing heat loss from your home will pay off in several ways. Lowering your winter energy bills is the most obvious benefit, but the things you do to reduce home heat loss also will reduce heat gain in the summer, so your air conditioning bills will go down, too. You also might extend the life of your heating and air conditioning equipment.'''
#     },
#     {
#         'title': 'Energy',
#         'image': 'static/assets/electricity.svg',
#         'content': '''The primary environmental effect of energy overuse is an increase in your carbon footprint, but there are simple changes you can make at home to avoid this. For example, if you keep devices plugged in and running when they're not in use, the result is an increase in electrical use and, consequently, a bump in the amount of greenhouse gases that enter the atmosphere. Leaving your laptop plugged in all the time will use nearly 300 kilowatt hours (kWh) of electricity each year, and a desktop computer left to idle will use more than 600 kW of electricity annually. Even leaving your fully charged cellphone attached to its charger can waste almost 20 kWh a year.
#
#         A natural consequence of overusing energy is increased costs for you. This can come in the form of fuel and energy bills; you will be paying more without an appreciable return on your investment. You may also risk lowering the expected lifespan of appliances and other electronics. When you have to replace spent devices, you further impact the environment by generating waste and purchasing replacement equipment. '''
#     },
#
# ]


@app.route("/")
def index():
    animation_info = list(mongo.db.animation.find())
    # for i in animation_info:
    #     mongo.db.animation.insert_one(i)
    return render_template("index.html", index_page=True,
                           animation_info=animation_info)


@app.route('/calendar')
def calendar():
    return render_template("calendar.html")


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
        validate_password = True if request.form.get(
            "password") == request.form.get("password2") else flash(
            "Passwords not matching")
        validate_password2 = True if request.form.get(
            'password_is_valid') == 'yes' else flash("Passwords not valid")
        if validate_password and validate_password2:
            register_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
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
        blog_list = mongo.db.blog.find(
            {"created_by": {'$eq': session['user']}})
        category_list = list(mongo.db.categories.find())
        return render_template("profile.html", blog_list=blog_list,
                               category_list=category_list)
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
    """
    Add a category
    """
    if "user" in session:
        if request.method == "POST":
            category_name = request.form.get("category_name")
            category_description = request.form.get("category_description")
            category = {
                "name": category_name,
                "description": category_description
            }
            mongo.db.categories.insert_one(category)
            return redirect(url_for("categories"))
        return render_template("add_category.html")
    else:
        return render_template('404.html'), 404


@app.route("/<category_id>/edit_category", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Edit a category
    """
    if "user" in session:
        if request.method == "POST":
            category_name = request.form.get("category_name")
            category_description = request.form.get("category_description")
            category = {
                "name": category_name,
                "description": category_description
            }
            mongo.db.categories.update_one({'_id': ObjectId(category_id)},
                                           {'$set': category})
            return redirect(url_for("categories"))
        category = mongo.db.categories.find_one(
            {'_id': ObjectId(category_id)})
        return render_template("edit_category.html",
                               category=category)
    else:
        return render_template('404.html'), 404


@app.route('/<category_id>/delete', methods=['GET', 'POST'])
def delete_category(category_id):
    """
    Delete a category
    """
    if "user" in session:
        blog_list = list(mongo.db.blog.find(
            {"categories": {"$all": [category_id, ]}}
        ))
        if not blog_list:
            category = mongo.db.categories.find_one(
                {'_id': ObjectId(category_id)})
            mongo.db.categories.delete_one({'_id': ObjectId(category_id)})
            flash('Successfully deleted {}'.format(category["name"]))
            return redirect(url_for('categories'))
        else:
            flash(
                'This category is referred to by blogs. It cannot be deleted until the associated blogs are removed first.')
            return redirect(url_for('categories'))
    else:
        return render_template('404.html'), 404


@app.route('/blog')
def blog():
    query_filter = None
    if request.args.get("filter"):
        query = request.args.get("filter")
        query_filter = mongo.db.categories.find_one(
            {"_id": ObjectId(query)})

        blog_list = list(mongo.db.blog.find(
            {"categories": {"$all": [query, ]}}
        ))
    else:
        blog_list = list(mongo.db.blog.find())
    category_list = list(mongo.db.categories.find())

    return render_template('blog.html', blog_list=blog_list,
                           category_list=category_list, filter=query_filter)


@app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    # Check if user is in session
    blog_categories = mongo.db.categories.find()
    if request.method == 'POST':
        if "user" in session:
            submit = {
                'categories': request.form.getlist('categories_list'),
                'title': request.form.get('title'),
                'blog_text': request.form.get('blog_text'),
                'created_by': session['user']
            }
            mongo.db.blog.insert_one(submit)
            flash("Record {} created".format(submit['title']))
            return redirect(url_for('blog'))
        else:
            return redirect(url_for("login"))
    return render_template('add_blog.html', categories=blog_categories)


@app.route('/edit_blog/<blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    single_blog = mongo.db.blog.find_one(
        {"_id": ObjectId(blog_id)})

    if "user" in session:
        blog_categories = list(mongo.db.categories.find())
        if request.method == 'POST':
            if "user" in session:
                if single_blog['created_by'] == session['user']:
                    submit = {
                        'categories': request.form.getlist('categories_list'),
                        'title': request.form.get('title'),
                        'blog_text': request.form.get('blog_text'),
                        'created_by': session['user']
                    }
                    mongo.db.blog.update_one({"_id": ObjectId(blog_id)},
                                             {"$set": submit})
                    flash("Record {} updated".format(submit['title']))
                    return redirect(url_for('profile'))
                else:
                    flash('You only allowed to remove your own records')
                    return redirect(url_for('profile'))
    else:
        return redirect(url_for("login"))
    return render_template('edit_blog.html', categories=blog_categories,
                           blog=single_blog)


@app.route('/delete_blog/<blog_id>')
def delete_blog(blog_id):
    if "user" in session:
        record = mongo.db.blog.find_one(
            {"_id": ObjectId(blog_id)}
        )
        if record['created_by'] == session['user']:
            mongo.db.blog.delete_many(
                {"_id": ObjectId(blog_id)}
            )
            flash('Successfully deleted {}'.format(record["title"]))
            return redirect(url_for('profile'))
        else:
            flash('You only allowed to remove your own records')
            return redirect(url_for('profile'))
    else:
        flash("You need to be logged in to perform this action")
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
