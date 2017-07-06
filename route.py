from flask import Flask, render_template

#create an instance of the flask class
app = Flask(__name__)

#map the url / to the function index
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

if __name__== "__main__":
    app.run(debug=True)