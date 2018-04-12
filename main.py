from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():

    user_name = ""
    email = ""

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    return render_template("home_page.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, user_name=user_name, email=email )

@app.route("/welcome", methods=["POST"])
def welcome():

    username_error = "" 
    password_error = "" 
    verify_error = "" 
    email_error = ""

    user_name = request.form["user_name"]
    email = request.form["email"]
    password = request.form["password"]
    verify = request.form["verify"]

    if len(user_name) < 3 or len(user_name) > 20 or (" ") in (user_name):
        username_error = "That's not a valid username"
    
    if len(password) < 3 or len(password) > 20 or (" ") in (password):
        password_error = "That's not a valid password"

    if len(verify) < 3 or len(verify) > 20 or (" ") in (verify) or len(verify) != len(password):
        verify_error = "Passwords don't match"

    if len(email) == 0:
        return render_template("home_page.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=user_name, email=email )    
           
    elif "@" not in email or "." not in email or (" ") in email:
        email_error = "That's not a valid email"
    
    if len(verify_error) > 0:
        return render_template("home_page.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=user_name, email=email )    
        
    if len(password_error) > 0:
        return render_template("home_page.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=user_name, email=email )    
        
    if len(email_error) > 0:
        return render_template("home_page.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=user_name, email=email )    
        
    if len(username_error) > 0:
        return render_template("home_page.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=user_name, email=email )  
   
    else: 
        return render_template("welcome_page.html", name=user_name)
        

app.run()