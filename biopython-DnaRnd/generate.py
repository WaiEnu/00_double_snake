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

def generate_origin(length,iteration):
    ittr = int(iteration)
    lens = int(length)
    origin=[]
    counter = ittr
    while counter > 0:
        pre_seq=genetics.rndn_sequence(lens)
        origin.extend(genetics.translate(pre_seq))
        counter -= 1
    return getTable(origin)

def generate_mutant(origin,base,locate,length):
    index = int(base)
    start = int(locate)
    end = int(length)
    mutate=[]
    for sequence in origin:
        pre_seq=genetics.one_flame_shift(sequence,index,start,end)
        mutate.extend(genetics.translate(pre_seq))
    return getTable(mutate)

def getTable(master):
    master_STT=getRow(master,'STT')
    master_STP=getRow(master,'STP')
    master_LEN=getRow(master,'LEN')
    master_COD=getRow(master,'codon')
    master_PRO=getRow(master,'protain')
    master_DNA=getRow(master,'DNA')
    master_CNA=getRow(master,'cDNA')
    master_RNA=getRow(master,'mRNA')
    return {'STT':master_STT,'STP':master_STP,'LEN':master_LEN,'codon':master_COD,'protain':master_PRO,'DNA':master_DNA,'cDNA':master_CNA,'mRNA':master_RNA}

def getRow(dic,str_obj):
    return [d.get(str_obj) for d in dic]

def make_table_sec(table_deta):
    table_ret_df=DataFrame(table_deta)
    table_df=table_ret_df[['DNA','mRNA']]
    table=table_df.to_html(header='true')
    return table

def make_read_sec(read_deta):
    read_ret_df=DataFrame(read_deta)
    read_df=read_ret_df[['codon','protain','mRNA']]
    read=read_df.to_html(header='true')
    return read

def make_graph_df(graph_deta):
    graph_ret_df=DataFrame(graph_deta)
    graph_df=graph_ret_df[['STT','STP','LEN']]
    return graph_df

# 生成した遺伝暗号の情報を見たい
# → 配列の長さを見よう
# → 開始位置を割り出せば大体の長さの見当がつく？
def make_graph_sec(graph_df,title):
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