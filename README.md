# Earthling

# Project overview

Greetings! We are the Earthlings, and this is our project to help save the only planet we have. As well as featuring a calendar with ideas of what you can do to help the earth each month, our site features a blog with the ability for users to log in to the site to contribute ideas, tips, and conversations that help keep the world turning. Users might visit this site for several reasons: to learn this month's promoted tip; to share ideas, thoughts and inspirations with other users; and to discuss these things. As such, the site features the ability to create an account, log in and out, and post from an account; the site also features authentication to securely facilitate this.

---

## Site features

The site features full registration, log-in and log-out functionality with authentication built into both the front and back end to facilitate this.

### Log-in, log-out, register and navbar

![Image of the navbar from the POV of a logged-out user](docs/readmeimages/navbarloggedout.png)

A user who is not logged in will see the above options in the navbar. The Home, Calendar and Blogs links are visible for all users, while Register and Log in will be displayed only for users not logged in.

![Image of the log in form](docs/readmeimages/registrationform.png)

Above is the form presented to log in to the site for a logged-out user. As you can see, the form carries an option to click a link to the register account page should a user not already have an account.

![Image of the navbar from the POV of a logged-in user](docs/readmeimages/navbarloggedin.png)

Above is what a user sees from the navbar when logged in to the site. From this, you can also see the flash message presented when a user has just logged in.

### Home page animation

![Image of the homepage animation](docs/readmeimages/homepageanimation.png)

The home page features an animation of moving buttons revolving around a central, stationary image. Clicking any of these buttons brings up a modal containing information on its theme, and good advice for site users to lower their impact on the planet by making changes relating to this theme.

### Categories maintenance (CRUD suite)

- The available list of categories to add to the blogs can be maintained from a menu option on the nav manu once signed in.
- The option is not available to users that are not logged in.
- From the List Categories page categories can be added, edited and deleted.
- They can only be deleted if no blogs are referring to them.

![Image of the list categories screen](docs/readmeimages/list-categories.jpg)
![Image of Add Category screen](docs/readmeimages/add-category.jpg)
![Image of Edit Category screen](docs/readmeimages/edit-category.jpg)


---

## Wireframes

| Desktop | Mobile |
| --- | --- |
| [Home page signed in](docs/wireframes/homedesktopsignedin.png), [Home page not signed in](docs/wireframes/homedesktopnotsignedin.png), [Home page as admin](docs/wireframes/homedesktopsignedinadmin.png) | [Home page](docs/wireframes/homemobile.png) |
| [Add suggestion](docs/wireframes/addsuggestion.png) | [Add suggestion](docs/wireframes/addsuggestion.png) |
| [Categories](docs/wireframes/categoriesdesktop.png) | [Categories](docs/wireframes/categoriesdesktop.png) |
| [Suggestions signed in](docs/wireframes/suggestionsdesktopsignedin.png), [Suggestions not signed in](docs/wireframes/suggestionsdesktopnotsignedin.png) | [Suggestions signed in](docs/wireframes/suggestionsdesktopsignedin.png), [Suggestions not signed in](docs/wireframes/suggestionsdesktopnotsignedin.png) |


---

## Technologies used

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

* [Werkzeug](https://wsgi.readthedocs.io/en/latest/what.html)
    * Werkzeug is a Web Server Gateway Interface web application library.

* [Jinja](https://www.palletsprojects.com/p/jinja/)
    * Jinja is a templating engine for Python, used to write Flask and other templating services.

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes for this project.

* [Git](https://git-scm.com/)
    * Git was used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.

* [Bootstrap 5](https://getbootstrap.com/)
    * Bootstrap is one of the most popular front-end open source toolkit and was used for ease of styling the Earthlings app.

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * This project was created in the Google Chrome browser, and as such Chrome was used as the default testing browser.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches our development version by checking features and screen layouts on both versions.

* [MongoDB](https://www.mongodb.com/)
    * MongoDB is where we host our NoSQL database.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.

* [Online-Convert](https://www.online-convert.com/)
    * Online-Convert was used to convert the png images to webp.

---

## Credits

* Content
    * Tips and suggestions used for the Monthly Eco Planner were collated from:
        * [Sustainability Mag](https://sustainabilitymag.com/top10/top-10-causes-global-warming)
        * [The Big Green K](https://thebiggreenk.com/blog/10-things-you-can-do-to-positively-impact-the-environment/)
        * [Collect My Cothes](https://collectmyclothes.co.uk/how-donating-clothes-helps-the-environment/)
        * [Sustrans.Org](https://www.sustrans.org.uk/our-blog/get-active/2020/in-your-community/five-tips-for-going-car-free)
        * [The Good Planet](https://thegoodplanet.org/2020/06/02/how-you-can-save-our-planet-by-deleting-emails)
        * [Country Living](https://www.countryliving.com/uk/homes-interiors/interiors/g25329535/eco-friendly-christmas-ideas-green-christmas/)
        * [Readers Digest](https://www.readersdigest.co.uk/lifestyle/home-garden/how-to-shop-sustainably)
        * [Greenpeace](https://www.greenpeace.org.uk/news/9-ways-reduce-plastic-use/)
        * [Panda.Org](https://wwf.panda.org/act/live_green/travel/on_vacation/)
        * [Volcanoes Safaris](https://volcanoessafaris.com/press/7-ways-to-make-your-travel-more-sustainable/)
        * [The Royal Horticultural Society](https://www.rhs.org.uk/gardening-for-the-environment/planet-friendly-gardening-tips)
        * [Lancaster University](https://www.lancaster.ac.uk/data-science-of-the-natural-environment/blogs/green-computing-a-contribution-to-save-the-environment)

* Media
    * [Adobe Stock](https://stock.adobe.com/uk/)
        * Some illustrations used for the Earthlings were licensed from Adobe.

---

## Acknowledgements

* Many thanks to the Code Institute Hackathon team for organizing these events that enables participants to collaborate with fellow student developers and alumni, experience sprint development and have fun along the way!

* We are Team Earthlings:
    * [Alex](https://github.com/alexandergrib)
    * [Daniel](https://github.com/xiaoniuniu89)
    * [Evelyn](https://github.com/evelynfoy)
    * [James](https://github.com/James-VT)
    * [Joy](https://github.com/JoyZadan)