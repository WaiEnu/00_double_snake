from flask import Flask, render_template, request, Markup, redirect
import pandas as pd
from pandas import DataFrame
import pandas.plotting as matrix
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
import genetics

app = Flask(__name__)

class DataStore():
    origin=None
    mutate=None
data=DataStore()

@app.route('/')
def index():
    data.origin = None
    data.mutate = None
    graph_o = make_graph_origin()
    graph_m = make_graph_mutate()
    return render_template('index.html',graph_o=graph_o,graph_m=graph_m)

@app.route('/generate', methods=['POST'])
def gen():
    length = request.form['length']
    iteration = request.form['iteration']
    locate = request.form['locate']
    base = request.form['base']

    data.origin = genetics.generate_origin(length,iteration)
    data.mutate = genetics.generate_mutant(genetics.getRow(data.origin,'DNA'),base,locate,length)  
 
    data_o = DataFrame(data.origin)
    data_m = DataFrame(data.mutate)
    table_o = make_table_sec(data_o)
    table_m = make_table_sec(data_m)
    read_o = make_read_sec(data_o)
    read_m = make_read_sec(data_m)
    graph_o = make_graph_origin()
    graph_m = make_graph_mutate()

    return render_template('index.html',table_o=table_o,table_m=table_m,read_o=read_o,read_m=read_m,graph_o=graph_o,graph_m=graph_m)

# @app.route("/plot/origin")
def make_graph_origin():
    src="" 
    if data.origin is not None:
        data_o = DataFrame(data.origin)
        src += "data:image/png:base64,"
        src += draw_graph(make_graph_sec(data_o),'origin')
    return src

# @app.route("/plot/mutate")
def make_graph_mutate():
    src= ""
    if data.mutate is not None:
        data_m =DataFrame(data.mutate)
        src += "data:image/png:base64,"
        src += draw_graph(make_graph_sec(data_m),'mutate')
    return src

def make_table_sec(table_ret_df):
    table_dp_df=table_ret_df[['DNA','mRNA','translate']]
    table_df=table_dp_df.drop_duplicates()
    table=table_df.to_html(header='true')
    return Markup(table)

def make_read_sec(read_ret_df):
    read_df=read_ret_df[['codon','protain','mRNA']]
    read=read_df.to_html(header='true')
    return Markup(read)

def make_graph_sec(graph_ret_df):
    graph_df=graph_ret_df[['STT','STP','LEN']]
    return graph_df

# 生成した遺伝暗号の情報を見たい
# → 配列の長さを見よう
# → 開始位置を割り出せば大体の長さの見当がつく？
def draw_graph(graph_df,title):
    fig = Figure()
    fig, axes = plt.subplots(2, 2, figsize=(6, 6))
    sns.scatterplot(x='STT', y='STP', data=graph_df, ax=axes[0,0])
    sns.scatterplot(x='STT', y='LEN', data=graph_df, ax=axes[0,1])
    sns.distplot(graph_df['LEN'], ax=axes[1,:])
    fig.tight_layout()
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    img_data = urllib.parse.quote(png_output.getvalue())
    return img_data

if __name__ == '__main__':
    app.debug = True
    app.run()