from flask import Flask, render_template, request, Markup, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import numpy as np
import generate

init_title="DNA Generator"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret' # CSRF対策でtokenの生成に必要

@app.route('/')
def index():
    return render_template('index.html',title="DNA Generator")

@app.route('/generate', methods=['POST'])
def gen():
    length = request.form['length']
    iteration = request.form['iteration']
    locate = request.form['locate']
    base = request.form['base']

    origin = generate.generate_origin(length,iteration)
    mutation = generate.generate_mutant(origin,base,locate,length)
    table_align = make_table(origin)
    table_mutate = make_table(mutation)
    graph_align = make_graph(origin)
    graph_mutate = make_graph(mutation)
    return render_template('index.html',table_align=table_align,table_mutate=table_mutate,graph_align=graph_align,graph_mutate=graph_mutate,title=init_title)

def make_table(align):
    table=generate.make_table_sec(align['table'])
    return Markup(table)

def make_graph(align):
    graph=generate.make_graph_sec(align['graph'])
    return Markup(graph)

if __name__ == '__main__':
    app.debug = True
    app.run()