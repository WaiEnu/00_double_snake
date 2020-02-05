from flask import Flask, render_template, request, Markup, redirect
import generate

app = Flask(__name__)

class DataStore():
    origin=None
    mutate=None
    isNull=True
data=DataStore()

@app.route('/')
def index():
    data.isNull=True
    return render_template('index.html',graph_o=None,graph_m=None)

@app.route('/generate', methods=['POST'])
def gen():
    length = request.form['length']
    iteration = request.form['iteration']
    locate = request.form['locate']
    base = request.form['base']

    data_o = generate.generate_origin(length,iteration)
    data_m = generate.generate_mutant(data_o['DNA'],base,locate,length)
    table_o = Markup(generate.make_table_sec(data_o))
    table_m = Markup(generate.make_table_sec(data_m))
    read_o = Markup(generate.make_read_sec(data_o))
    read_m = Markup(generate.make_read_sec(data_m))
    graph_o = generate.make_graph_df(data_o)
    graph_m = generate.make_graph_df(data_m)
    data.origin=graph_m
    data.mutate=graph_o
    data.isNull=False
    return render_template('index.html',table_o=table_o,table_m=table_m,read_o=read_o,read_m=read_m,graph_o=graph_o,graph_m=graph_m)

@app.route("/plot/origin")
def make_graph_origin():
    if data.isNull is False:
        return generate.make_graph_sec(data.origin,'origin')
    else:
        return ''

@app.route("/plot/mutate")
def make_graph_mutate():
    if data.isNull is False:
        return generate.make_graph_sec(data.mutate,'mutate')
    else:
        return ''

if __name__ == '__main__':
    app.debug = True
    app.run()