import csv
from flask import abort
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path)
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(404)

app.route('/<row_id>/')(detail)

app.route('/')(index)

app.run(debug=True, use_reloader=True)
