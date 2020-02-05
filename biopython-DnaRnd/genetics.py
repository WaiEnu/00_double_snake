from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
import random
import re
import detaset

dna=detaset.dna()
dna_len=len(dna)
sep=detaset.sep_str()
amino=detaset.amino()

def rndn_sequence(lens):
    rnd_str=''
    for i in range(0,lens):
        rnd_str+=random.choice(dna)
    return rnd_str

def one_flame_shift(mutable_seq,index,start,end):
    out_before = mutable_seq[0:start-1]
    out_after = mutable_seq[start:end-1]
    out=''
    if(index < dna_len):
        out = out_before + dna[index-1] + out_after
    else:
        out = out_before[:-1] + out_after
    return out

def transcribe(sequence):
    DNA_sequence = Seq(sequence, IUPAC.ambiguous_dna)
    cDNA_sequence = DNA_sequence.complement()
    mRNA_sequence = DNA_sequence.transcribe()
    return {'DNA':DNA_sequence,'cDNA':cDNA_sequence,'mRNA':mRNA_sequence}

def translate(sequence):
    read_seq=str(sequence)
    start = re.finditer(r"AUG",read_seq)
    result=[]
    for s in start:
        point=s.start()
        tmp=make_codon(read_seq,point)
        result.append(tmp)
    return result

def make_codon(read_seq,start):
    k=3
    idx=0
    result=[]
    pre_codon = read_seq[start::]
    result.append(start)
    for i in range(0, len(pre_codon), k):
        codon = pre_codon[i:i+k]
        idx=start+i
        if codon in amino["x"]:
            result.append(start+i)
            return formatResult(result,read_seq)
        elif len(codon)<3 :
            result.append(start+i)
            return formatResult(result,read_seq)
        else:
            result.append(codon)
    result.append(idx)
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
    codon=result[1:len(result)-1]
    prot=read_codon(codon)
    start=result[0]
    stop=result[-1]
    return {'STT':start,'STP':stop,'LEN':len(codon),'codon':sep.join(codon),'protain':sep.join(prot),'mRNA':read_seq}
