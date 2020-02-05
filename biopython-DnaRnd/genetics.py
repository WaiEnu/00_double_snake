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

def dic_nuc(sequence):
    DNA_sequence = Seq(sequence, IUPAC.ambiguous_dna)
    cDNA_sequence = DNA_sequence.complement()
    mRNA_sequence = DNA_sequence.transcribe()
    return {'DNA':str(DNA_sequence),'cDNA':str(cDNA_sequence),'mRNA':str(mRNA_sequence)}

def translate(sequence):
    dic=dic_nuc(sequence)
    start = re.finditer(r"AUG",dic['mRNA'])
    result=[]
    for s in start:
        point=s.start()
        tmp=make_codon(dic,point)
        result.append(tmp)
    return result

def make_codon(dic,start):
    k=3
    idx=0
    result=[]
    read_seq=dic['mRNA']
    pre_codon = read_seq[start::]
    for i in range(0, len(pre_codon), k):
        codon = pre_codon[i:i+k]
        idx=start+i
        if codon in amino["x"]:
            return formatResult(start,idx,result,dic)
        elif len(codon)<3 :
            return formatResult(start,idx,result,dic)
        else:
            result.append(codon)
    return formatResult(start,idx,result,dic)

def read_codon(codon):
    read_seq= Seq(codon, IUPAC.ambiguous_rna)
    result =read_seq.translate()
    return str(result)

def formatResult(start,stop,codon_list,dic):
    codon=sep.join(codon_list)
    prot=read_codon(''.join(codon_list))
    dic = {'STT':start,'STP':stop,'LEN':len(prot),'codon':codon,'protain':prot,'DNA':dic['DNA'],'cDNA':dic['cDNA'],'mRNA':dic['mRNA']}
    return dic
