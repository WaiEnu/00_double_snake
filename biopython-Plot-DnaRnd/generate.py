import detaset
import transcription
import mutation
import translation
import caliculate

def generate_origin(length,iteration):
    ittr = int(iteration)
    dic_seq=[]
    while ittr>0:
        pre_seq=sequence(length)
        dic_seq.append(out_seq(pre_seq))
        ittr-=1
    return getDeta(dic_seq,length)

def generate_mutant(dic_origin,base,locate,length):
    origin=getRowDna(dic_origin)
    dic_seq=[]
    for sequence in origin:
        pre_seq=mutate(sequence,base,locate,length)
        dic_seq.append(out_seq(pre_seq))
    return getDeta(dic_seq,length)

def getDeta(dic,length):
    table=getTableDeta(dic)
    read=getPlotDeta(dic)
    graph=getGraphDeta(read,length)
    deta={'table':table,'graph':graph,'read':read}
    return deta

def sequence(length):
    maxi = int(length)
    output=transcription.sequence(maxi)
    return output

def mutate(sequences,base,locate,length):
    index = int(base)
    point = int(locate)
    end = int(length)
    output=mutation.one_flame_shift(sequences,index,point,end)
    return output

def out_seq(sequence):
    DNA_sequence = sequence
    cDNA_sequence = transcription.complement(sequence)
    mRNA_sequence = transcription.messenger(sequence)
    dic = {'DNA':DNA_sequence,'cDNA':cDNA_sequence,'mRNA':mRNA_sequence}
    return dic

def getPlotDeta(dic):
    read_seq = getRows(dic,'mRNA')
    read_list = []
    for seq in read_seq:
        tran=translation.translate(seq)
        read_list.extend(tran)
    return read_list

def getGraphDeta(dic,length):
    deta=caliculate.align_deta(getRows(dic,'protain'),length)
    return deta

def getTableDeta(dic):
    master_DNA=getRows(dic,'DNA')
    master_CNA=getRows(dic,'cDNA')
    master_RNA=getRows(dic,'mRNA')
    dic = {'DNA':master_DNA,'cDNA':master_CNA,'mRNA':master_RNA}
    return dic

def getRows(dic,str_obj):
    obj = [d.get(str_obj) for d in dic]
    return obj

def getRowDna(dictionary):
    deta=dictionary['table']
    seq=deta['DNA']
    return seq

def make_table_sec(table_deta):
    return caliculate.make_table_sec(table_deta)

def make_read_sec(read_deta):
    return caliculate.make_read_sec(read_deta)

def get_graph(graph_deta,keys):
    return caliculate.get_graph(graph_deta,keys)
