#Main imports and package dependencies
import sqlite3
import datetime
from flask import Flask, jsonify, render_template
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.embed import components


app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to charting with Bokeh! This data is from someones greenhouse in PyData class!'

@app.route('/chart')
def chart():
    p = figure(plot_width=1000, plot_height=800,
    x_axis_type="datetime")
    #add a line renderer
    x = []
    y = []
    all_data = get_data()
    for value in all_data:
        date = datetime.datetime.fromtimestamp(value[0])
        x.append(date)
        y.append(value[1])
    # create chart
    p.line(x, y, line_width=2)
    #create static files
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    script, div = components(p)
    # render template
    return render_template(
        'chart.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources)


@app.route('/data')
def get_data():
    # Open database connection
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        # Generate SQL query
        c.execute("""SELECT * FROM greenhouse""")
        rows = c.fetchall()
    return rows


if __name__ == '__main__':
    app.run(debug=True)
