from flask import Flask, render_template, request, Markup, redirect
import generate

init_title="DNA Generator"

app = Flask(__name__)

class DataStore():
    origin=None
    mutate=None
data=DataStore()

@app.route('/')
def index():
    origin = returnGpaph(None,'origin')
    mutate = returnGpaph(None,'mutate')
    return render_template('index.html',origin=origin,mutate=mutate)

@app.route('/generate', methods=['POST'])
def gen():
    length = request.form['length']
    iteration = request.form['iteration']
    locate = request.form['locate']
    base = request.form['base']

    data_origin = generate.generate_origin(length,iteration)
    data_mutate = generate.generate_mutant(data_origin,base,locate,length)

    origin = returnGpaph(data_origin['graph'],'origin')
    mutate = returnGpaph(data_mutate['graph'],'mutate')

    table_origin = Markup(generate.make_table_sec(data_origin['table']))
    table_mutate = Markup(generate.make_table_sec(data_mutate['table']))
    read_origin = Markup(generate.make_read_sec(data_origin['read']))
    read_mutate = Markup(generate.make_read_sec(data_mutate['read']))

    return render_template('index.html',table_origin=table_origin,table_mutate=table_mutate,read_origin=read_origin,read_mutate=read_mutate,origin=origin,mutate=mutate)

def returnGpaph(graph_deta,key):
    src= ""
    if graph_deta is not None:
        src += "data:image/png:base64,"
        src += generate.get_graph(graph_deta,key)
    return src

if __name__ == '__main__':
    app.debug = True
    app.run()