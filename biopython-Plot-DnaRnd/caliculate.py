import detaset
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

sep=detaset.sep_str()

def align_deta(align,length):
    dic=[]
    for a in align:
        dic.append(prosess(a,length))
    return dic

def prosess(a,l):
    prot=a.split(sep)
    lens=len(prot)-2
    start=int(prot[0])+1
    stop= int(l) if prot[-1].isalpha() else int(prot[-1])+1
    return {'STT':start,'STP':stop,'LEN':lens}

def make_table_sec(table_deta):
    table_df=pd.DataFrame(table_deta)
    table_ret_df=table_df[['DNA','mRNA']]
    table=table_ret_df.to_html(header='true')
    return table

def make_read_sec(read_deta):
    read_df=pd.DataFrame(read_deta)
    read_ret_df=read_df[['codon','protain']]
    read=read_ret_df.to_html(header='true')
    return read

def get_graph(graph_deta,keys):
    graph_df=pd.DataFrame(graph_deta)
    fig = Figure()
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(9,3))
    sns.scatterplot(x='STT', y='STP', data=graph_df, ax=axes[0])
    sns.scatterplot(x='STT', y='LEN', data=graph_df, ax=axes[1])
    sns.distplot(graph_df['LEN'], kde=True, rug=True, ax=axes[2])
    fig.tight_layout()
    fig.suptitle(keys)
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    img_data = urllib.parse.quote(png_output.getvalue())
    return img_data