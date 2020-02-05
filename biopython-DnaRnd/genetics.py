from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
import random
import re

amino = {
"F":["UUU","UUC"],
"L":["UUA","UUG","CUU","CUC","CUA","CUG"],
"I":["AUU","AUC","AUA"],
"M":["AUG"],
"V":["GUU","GUC","GUA","GUG"],
"S":["UCU","UCC","UCA","UCG","AGU","AGC"],
"P":["CCU","CCC","CCA","CCG"],
"T":["ACU","ACC","ACA","ACG"],
"A":["GCU","GCC","GCA","GCG"],
"Y":["UAU","UAC"],
"H":["CAU","CAC"],
"Q":["CAA","CAG"],
"N":["AAU","AAC"],
"K":["AAA","AAG"],
"D":["GAU","GAC","GAA","GAG"],
"E":["GAA","GAG"],
"C":["UGU","UGC"],
"W":["UGG"],
"R":["CGU","CGC","CGA","CGG","AGA","AGG"],
"G":["GGU","GGC","GGA","GGG"],
"x":["UAA","UAG","UGA"]
}
dna = ["A","G","C","T"]
sep='-'
sepN=''

def rndn_sequence(lens):
    return sepN.join([ random.choice(dna) for x in range(lens) ])

def one_flame_shift(mutable_seq,index,start,end):
    out_before = mutable_seq[0:start-1]
    out_after = mutable_seq[start:end-1]
    out=''
    if(index < len(dna)):
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
