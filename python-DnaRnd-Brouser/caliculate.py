import detaset
import pandas as pd
import pandas.plotting as matrix
import matplotlib as mpl
import matplotlib.pyplot as plt
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

def make_graph_sec(graph_deta):
    graph_df=pd.DataFrame(graph_deta)
    graph=graph_df.to_json()
    return graph