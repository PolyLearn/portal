from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/products")
def products():
    return render_template('products.html')

@app.route("/concept")
def concept():
    return render_template('concept.html')

if __name__ == "__main__":
    app.run()
