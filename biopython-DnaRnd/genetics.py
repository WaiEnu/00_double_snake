from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from random import choice
import re

dna = "AGCT"
stop_str="@"

def rndn_sequence(lens, sep=''):
    return sep.join([ choice(dna) for x in range(lens) ])

def one_flame_shift(mutable_seq,index,start,end):
    out_before = mutable_seq[0:start-1]
    out_after = mutable_seq[start:end-1]
    return out_before + dna[index-1] + out_after if index < len(dna) else out_before[:-1] + out_after

def translate(sequence):
    DNA_seq = Seq(sequence, IUPAC.ambiguous_dna)
    cDNA_seq = DNA_seq.complement()
    mRNA_seq = DNA_seq.transcribe()
    result=[]
    for i in range(0,3):
        pre_seq=mRNA_seq[i::].translate(stop_symbol=stop_str)
        start = re.finditer(r"M",str(pre_seq))
        for s in start:
            point=s.start()
            tmp=make_codon(point,mRNA_seq[point::],pre_seq[point::])
            tmp.update({'DNA':str(DNA_seq),'cDNA':str(cDNA_seq),'mRNA':str(mRNA_seq)})
            result.append(tmp)
    return result

def make_codon(start,read_seq,pre_codon):
    idx=0
    for i in range(0, len(pre_codon)):
        idx=start+i*3
        if pre_codon[i] == stop_str:
            return formatResult(start,idx,read_seq[::idx],read_codon(pre_codon[::idx]))
    return formatResult(start,idx,read_seq[::idx],read_codon(pre_codon[::idx]))

def read_codon(codon, sep='-' ,k=3):
    return sep.join([codon[i:i+k] for i in range(0,len(codon),k)])

def formatResult(start,stop,prot,codon):
    return {'STT':start,'STP':stop,'LEN':len(prot),'codon':codon,'protain':prot}
