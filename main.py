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

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/pedagogie")
def pedagogie():
    return render_template('pedagogie.html')

if __name__ == "__main__":
    app.run()
