# Earthling

# Project overview

Greetings! We are the Earthlings, and this is our project to help save the only planet we have. As well as featuring a calendar with ideas of what you can do to help the earth each month, our site features a blog with the ability for users to log in to the site to contribute ideas, tips, and conversations that help keep the world turning. Users might visit this site for several reasons: to learn this month's promoted tip; to share ideas, thoughts and inspirations with other users; and to discuss these things. As such, the site features the ability to create an account, log in and out, and post from an account; the site also features authentication to securely facilitate this.

# Site features

The site features full registration, log-in and log-out functionality with authentication built into both the front and back end to facilitate this.

![Image of the navbar from the POV of a logged-out user](docs/readmeimages/navbarloggedout.png)

A user who is not logged in will see the above options in the navbar. The Home, Calendar and Blogs links are visible for all users, while Register and Log in will be displayed only for users not logged in.

![Image of the log in form](docs/readmeimages/registrationform.png)

Above is the form presented to log in to the site for a logged-out user. As you can see, the form carries an option to click a link to the register account page should a user not already have an account.

![Image of the navbar from the POV of a logged-in user](docs/readmeimages/navbarloggedin.png)

Above is what a user sees from the navbar when logged in to the site. From this, you can also see the flash message presented when a user has just logged in.

---

## Credits

### Technologies used

* Languages:
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back end programming of the site.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    * Flask was used to handle the templating for the site.

* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
    * Flask-PyMongo provides MongoDB support for Flask applications.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [dnspython](https://www.dnspython.org/)
    * Dnspython is a DNS toolkit for python.

* [Werkezeug](https://wsgi.readthedocs.io/en/latest/what.html)
    * Werkzeug is a Web Server Gateway Interface web application library.

* [Jinja](https://www.palletsprojects.com/p/jinja/)
    * Jinja is a templating engine for Python, used to write Flask and other templating services.

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes for this project. 

* [Git](https://git-scm.com/)
    * Git was used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * This project was created in the Google Chrome browser, and as such Chrome was used as the default testing browser.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches our development version by checking features and screen layouts on both versions.

* [MongoDB](https://www.mongodb.com/)
    * MongoDB is where we host our NoSQL database.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.
