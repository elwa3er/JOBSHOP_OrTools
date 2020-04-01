from flask import Flask, request, render_template,url_for
import os
import matplotlib
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
    fig = ff.create_gantt(df)
    fig.show()
    return render_template('gantt.html')


if __name__ == "__main__":
    app.run()