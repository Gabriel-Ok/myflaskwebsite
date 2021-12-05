from flask import *
from datetime import datetime
from flask_assets import Bundle, Environment
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome


app = Flask(__name__)
Bootstrap(app)
assets = Environment(app)
fa = FontAwesome(app)

js = Bundle('jquery.min.js', 'browser.min.js', 'breakpoints.min.js','util.js','main.js'
            , output='gen/all.js')
assets.register('all_js', js)
css = Bundle('noscript.css', 'main.css',output='gen/all.css')
assets.register('all_css', css)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/navbar')
def menubar():
    return render_template('navbar.html')



if __name__ == '__main__':
    app.run(debug=True)
