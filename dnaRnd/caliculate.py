import detaset
import pandas as pd
import pandas.plotting as matrix
import matplotlib as mpl
import matplotlib.pyplot as plt
import io

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
    stop= str(l) if prot[-1].isalpha() else int(prot[-1])+1
    return {'STT':start,'STP':stop,'LEN':lens}

def make_table_sec(table_deta):
    table_df=pd.DataFrame(table_deta)
    table_ret_df=table_df[['DNA','mRNA']]
    table=table_ret_df.to_html(header='true')
    return table

def make_graph_sec(graph_deta):
    graph_df=pd.DataFrame(graph_deta)
    sttTostp_df=graph_df[['STT','STP']]
    stpTolen_df=graph_df[['LEN','STP']]
    graph=sttTostp_df.to_html(header='true')+stpTolen_df.to_html(header='true')
    return graph