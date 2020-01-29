from flask import Flask, render_template, request, Markup, redirect, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import generate
import json

init_title="DNA Generator"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret' # CSRF対策でtokenの生成に必要

class DataStore():
    origin=None
    mutate=None
data=DataStore()

@app.route('/')
def index():
    data.origin = None
    data.mutate = None
    origin = data.origin
    mutate = data.mutate
    return render_template('index.html',origin=origin,mutate=mutate)

@app.route('/generate', methods=['POST'])
def gen():
    length = request.form['length']
    iteration = request.form['iteration']
    locate = request.form['locate']
    base = request.form['base']

    data_origin = generate.generate_origin(length,iteration)
    data_mutate = generate.generate_mutant(data_origin,base,locate,length)

    data.origin = data_origin['graph']
    data.mutate = data_mutate['graph']
    origin = data.origin
    mutate = data.mutate
    table_origin = Markup(generate.make_table_sec(data_origin['table']))
    table_mutate = Markup(generate.make_table_sec(data_mutate['table']))
    read_origin = Markup(generate.make_read_sec(data_origin['read']))
    read_mutate = Markup(generate.make_read_sec(data_mutate['read']))

    return render_template('index.html',table_origin=table_origin,table_mutate=table_mutate,read_origin=read_origin,read_mutate=read_mutate,origin=origin,mutate=mutate)
 
@app.route("/get-origin",methods=["GET","POST"])
def returnOriginData():
    f=data.origin
    return jsonify(f)

@app.route("/get-mutate",methods=["GET","POST"])
def returnMutateData():
    f=data.mutate
    return jsonify(f)
 
if __name__ == '__main__':
    app.debug = True
    app.run()