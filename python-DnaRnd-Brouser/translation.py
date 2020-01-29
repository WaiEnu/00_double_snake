import detaset
import re

amino=detaset.amino()
sep=detaset.sep_str()

def translate(read_seq):
    result=make_codon_set(read_seq)
    return result

def make_codon_set(read_seq):
    # start = read_seq.find("AUG")
    start = re.finditer(r"AUG",read_seq)
    dic=[]
    for s in start:
        tmp=make_codon(read_seq,s.start())
        dic.append(tmp)
    return dic

def make_codon(read_seq,start):
    k=3
    result=[]
    pre_codon = read_seq[start::]
    result.append(str(start))
    for i in range(0, len(pre_codon), k):
        codon = pre_codon[i:i+k]
        if codon in amino["x"]:
            result.append(str(start+i))
            return formatResult(result,read_seq)
        elif len(codon)<3 :
            result.append(str(start+i))
            return formatResult(result,read_seq)
        else:
            result.append(codon)
    return formatResult(result,read_seq)

def read_codon(codon_list):
    result =[]
    for i in range(0,len(codon_list)):
        aminosan=codon_list[i]
        aminosan_check = [k for k, v in amino.items() if codon_list[i] in v]
        if len(aminosan_check) != 0:
            aminosan = aminosan_check[0]
        result.append(aminosan)
    return result

def formatResult(result,read_seq):
    codon=result
    prot=read_codon(result)
    return {'codon':sep.join(codon),'protain':sep.join(prot),'read':read_seq}