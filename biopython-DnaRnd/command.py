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
import generate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',graph_o=None,graph_m=None)

@app.route('/generate', methods=['POST'])
def gen():
    length = request.form['length']
    iteration = request.form['iteration']
    locate = request.form['locate']
    base = request.form['base']

    data_o = generate.generate_origin(length,iteration)
    data_m = generate.generate_mutant(data_o['table']['DNA'],base,locate,length)
    table_o = make_table_sec(data_o['table'])
    table_m = make_table_sec(data_m['table'])
    read_o = make_read_sec(data_o['read'])
    read_m = make_read_sec(data_m['read'])
    graph_o = make_graph_origin(data_o['read'])
    graph_m = make_graph_mutate(data_m['read'])
    return render_template('index.html',table_o=table_o,table_m=table_m,read_o=read_o,read_m=read_m,graph_o=graph_o,graph_m=graph_m)

def make_table_sec(table_deta):
    table_ret_df=DataFrame(table_deta)
    table_df=table_ret_df[['DNA','mRNA']]
    table=table_df.to_html(header='true')
    return Markup(table)

def make_read_sec(read_deta):
    read_ret_df=DataFrame(read_deta)
    read_df=read_ret_df[['codon','protain','mRNA']]
    read=read_df.to_html(header='true')
    return Markup(read)

# 生成した遺伝暗号の情報を見たい
# → 配列の長さを見よう
# → 開始位置を割り出せば大体の長さの見当がつく？
@app.route("/plot/origin")
def make_graph_origin(graph_deta):
    return make_graph_sec(graph_deta,'origin')

@app.route("/plot/mutate")
def make_graph_mutate(graph_deta):
    return make_graph_sec(graph_deta,'mutate')

def make_graph_sec(graph_deta,title):
    graph_ret_df=DataFrame(graph_deta)
    graph_df=graph_ret_df[['STT','STP','LEN']]
    fig = Figure()
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    sns.scatterplot(x='STT', y='STP', data=graph_df, ax=axes[0,0])
    sns.scatterplot(x='STT', y='LEN', data=graph_df, ax=axes[1,0])
    sns.countplot(x="LEN", data=graph_df)
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    img_data = urllib.parse.quote(png_output.getvalue())
    return img_data

def get_psq_length(df):
    return ((df['STP']-df['STT'])/3)

if __name__ == '__main__':
    app.debug = True
    app.run()