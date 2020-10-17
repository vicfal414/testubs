import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/dash")
    def dash():
        return render_template("userdashboard.html")

    @app.route("/challenge")
    def chall():
        return render_template("challenge.html")

    @app.route("/friends")
    def friend():
        return render_template("friends.html")

  #  @app.route("/login")
  #  def login():
  #      return render_template("login.html")
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if (request.form['username'] != 'test') or request.form['password'] != 'test': error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                flash('You are logged in.')
                return redirect(url_for('home'))
        return render_template('login.html', error=error)
     
    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You are logged out.')
        return redirect(url_for('home'))
    
    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    @app.route("/css")
    def css():
        return render_template("static/css/style.css")

    return app


# database
# import os

# from flask import Flask
# from flask import render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import mysql.connector

# app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'myDB'

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     @app.route("/")
#     def home():
#         return render_template("index.html")

#     @app.route("/dash")
#     def dash():
#         return render_template("userdashboard.html")

#     @app.route("/challenge")
#     def chall():
#         return render_template("challenge.html")

#     @app.route("/friends")
#     def friend():
#         return render_template("friends.html")

#     @app.route("/login", methods=['GET', 'POST'])
#     def login():
#         msg = ''
#         if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#             username = request.form['username'] 
#             password = request.form['password']
#             #Check if acc exists
#             cursor = mysql.connector.connect(user='root', database='accounts')

#             cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password, ))
#             account = cursor.fetchone()

#             if account:
#                 #Current session
#                 session = {}
#                 session['loggedin'] = True
#                 session['id'] = account['id']
#                 session['username'] = account['username']

#                 return redirect(url_for('home')) 
#             else:
#                 #Error
#                 msg = 'Incorrect username/password'

#         return render_template("login.html", msg=msg)

#     @app.route("/signup")
#     def signup():
#         return render_template("signup.html")

#     @app.route("/css")
#     def css():
#         return render_template("static/css/style.css")

#     return app


# original
# import os

# from flask import Flask
# from flask import render_template


# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     @app.route("/")
#     def home():
#         return render_template("index.html")

#     @app.route("/dash")
#     def dash():
#         return render_template("userdashboard.html")

#     @app.route("/challenge")
#     def chall():
#         return render_template("challenge.html")

#     @app.route("/friends")
#     def friend():
#         return render_template("friends.html")

#     @app.route("/login")
#     def login():
#         return render_template("login.html")

#     @app.route("/signup")
#     def signup():
#         return render_template("signup.html")

#     @app.route("/css")
#     def css():
#         return render_template("static/css/style.css")

#     return app
