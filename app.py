from flask import Flask
from flask import render_template
app = Flask(__name__)


def index():
    template = 'index.html'
    return render_template(template)


app.route('/')(index)

app.run(debug=True, use_reloader=True)
