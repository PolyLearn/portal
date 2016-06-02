from flask import Flask, render_template
from flask_frozen import Freezer
from htmlmin.minify import html_minify
from flask_sitemap import Sitemap
import sys

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    FREEZER_RELATIVE_URLS=True,
    SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True,
)

ext = Sitemap(app=app)
freezer = Freezer(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/404.html')
def static_404():
    return render_template('404.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/products.html")
def products():
    return render_template('products.html')

@app.route("/concept.html")
def concept():
    return render_template('concept.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/thanks.html")
def thanks():
    return render_template('thanks.html')

@app.route("/pedagogie.html")
def pedagogie():
    return render_template('pedagogie.html')




@app.context_processor
def utility_processor():
    def app_url(app):
        return u'https://{}.polylearn.co'.format(app)
    return dict(app_url=app_url)

@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if (response.content_type == u'text/html; charset=utf-8'):
        response.direct_passthrough = False
        response.data = html_minify(response.data)
    return response


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        with open("build/sitemap.xml") as f:
             sitemap = f.read()
        with open("build/sitemap.xml", "w") as f:
             f.write(sitemap.replace("http://localhost/", "https://polylearn.co/"))
    else:
        app.run()
