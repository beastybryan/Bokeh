#https://www.blog.pythonlibrary.org/2016/07/27/python-visualization-with-bokeh/

from bokeh.plotting import figure, output_file, show

output_file("/home/bryan/pydata/flask-bokeh/test.html")

x = range(1, 6)
y = [10, 5, 7, 1, 6]
plot = figure(title='Line example', x_axis_label='x', y_axis_label='y')
plot.line(x, y, legend='Test', line_width=4)
show(plot)
