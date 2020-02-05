from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
import random
import re
import detaset

dna=detaset.dna()
dna_len=len(dna)
sep=detaset.sep_str()
sepN=detaset.sepN_str()
amino=detaset.amino()

def rndn_sequence(lens):
    return sepN.join([ random.choice(dna) for x in range(lens) ])

def one_flame_shift(mutable_seq,index,start,end):
    out_before = mutable_seq[0:start-1]
    out_after = mutable_seq[start:end-1]
    out=''
    if(index < dna_len):
        out = out_before + dna[index-1] + out_after
    else:
        out = out_before[:-1] + out_after
    return out

def translate(sequence):
    DNA_seq = Seq(sequence, IUPAC.ambiguous_dna)
    cDNA_seq = DNA_seq.complement()
    mRNA_seq = DNA_seq.transcribe()
    start = re.finditer(r"AUG",mRNA_seq)
    result=[]
    for s in start:
        point=s.start()
        tmp=make_codon(mRNA_seq[point::],point)
        tmp.update({'DNA':str(DNA_seq),'cDNA':str(cDNA_seq),'mRNA':str(mRNA_seq)})
        result.append(tmp)
    return result

def make_codon(pre_codon,start):
    k=3
    idx=0
    result=[]
    for i in range(0, len(pre_codon), k):
        codon = pre_codon[i:i+k]
        idx=start+i
        if codon in amino["x"] or len(codon)<3 :
            return formatResult(start,idx,result)
        else:
            result.append(codon)
    return formatResult(start,idx,result)

def read_codon(codon):
    read_seq= Seq(codon, IUPAC.ambiguous_rna)
    result =read_seq.translate()
    return str(result)

def formatResult(start,stop,codon_list):
    codon=sep.join(codon_list)
    prot=read_codon(sepN.join(codon_list))
    dic = {'STT':start,'STP':stop,'LEN':len(prot),'codon':codon,'protain':prot}
    return dic
