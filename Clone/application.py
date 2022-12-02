from flask import Flask, render_template
import sys
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("hello.html")

if __name__ == "__main__":
    application.run(host = '0.0.0.0')

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'