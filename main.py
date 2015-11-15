from flask import Flask, render_template
from flask_frozen import Freezer
from htmlmin.minify import html_minify
import sys

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    FREEZER_RELATIVE_URLS=True
)
freezer = Freezer(app)

@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if (not app.debug) and (response.content_type == u'text/html; charset=utf-8'):
        response.set_data(
            html_minify((response.get_data(as_text=True)))
        )
    return response

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

@app.route("/thanks")
def thanks():
    return render_template('thanks.html')

@app.route("/pedagogie")
def pedagogie():
    return render_template('pedagogie.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
