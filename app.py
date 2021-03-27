from flask import Flask, redirect, url_for, render_template, request, redirect, session
from db_connector.db_connector import connect_to_database, execute_query
# from datetime import datetime 
app = Flask(__name__)

# home
@app.route("/home")
def home():
    return render_template("front_page.html")

# log in
@app.route("/login", methods=["GET", "POST"])
def login()
    if request.method == "POST":
        # need a connect to db variable (function assigned to var)
        db = connect_to_db()
        # get variables
        username = request.form['username']
        password = request.form['password']
        #query
        get_user = "SELECT * from users WHERE username = %s AND password=%s;"
        #find to db
        db.execute(db_connection, get_all_username_query, data)
        acct = db.fetchone()
        if acct: # result not NULL -> credentials exist
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # change below to redirect to get started page
            return redirect(url_for('getStarted'))
        else:
            msg = "incorrect username/password"
    return render_template("login.html", msg) # create msg var in html page

# log out 
@app.route("/logout")
def logout():
    # remove session data - logs user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # redirect to login page
    return redirect(url_for('login'))

# create account
@app.route("/createAccount", methods=["GET", "POST"])
def create():
    # need a connect to db variable (function assigned to var)
    db = connect_to_db()
    if request.method == "POST":
        # need a select query to check if username is already taken
        username = request.form['username']
        password = request.form['password']
        get_all_username_query = "SELECT username from users WHERE username = %s;"
        data = (username)
        db.execute(get_all_username_query, data)
        acct = db.fetchone()
        if acct:
            msg = "Account already exist"
        elif not re.match(r'[A-Za-z0-09]+', username):
            msg = 'Username must contain only characters and numbers'
        elif not username or not password:
            msg = 'Fill out the form'
        else:
            insert_account_query = "INSERT INTO users (username, password) VALUES (%s,%s);"
            db.execute_query(insert_account_query, data)
            msg = 'You have successfully registered'
        # need to log the user in automatically and redirect to get_started if time allows
    return render_template("createAccount.html", msg)

# my_data
@app.route("/myData", methods=["POST", "GET"])
def my_data():
    # need a connect to db with variable (function assigned to var)
    db = connect_to_db()
    # need do a select query with session id as filter
    session_id = request.form['tbd'] # change this 
    session_query = "SELECT * from combined_table WHERE session_id = %s;"
    data = (session_id)
    # results from select query execution
    res = db.execute_query(session_query, data).fetchall()
    return render_template("my_data.html", res)

# get started
@app.route("/getStarted", methods=["POST", "GET"])
def get_started():
    # need a connect to db with variable (function assigned to var)
    db = connect_to_db()

    # select query with title of paper
    get_title_query = "SELECT title FROM acad_papers WHERE title = %s;"
    # insert query with title of paper
    insert_pdf = "INSERT INTO acad_papers (title) VALUES (%s);"
    # process paper - use model 
    # GET
    if request.method == "GET":
        # get variables 
        title = request.form['search_by_paper_title']
        # execute query
        data = (title)
        db.execute(get_title_query, data)
        res_paper = db.fetchone()
        # process if paper found
        if paper:
            # process paper thru model 
            pass
        # else show not found
        else:
            msg = "no paper found"
    # POST 
    elif request.method == "POST":
        # pre-process paper with the functions and shiz
        pass
        # need to insert title and process the title thru model
        # results need to be shown to user so render after this
    
    return render_template("get_started.html")
