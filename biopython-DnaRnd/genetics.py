from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from random import choice
import re

dna = "AGCT"
start_str="M"
stop_str="@"
stop_list=["UAA","UAG","UGA"]

def generate_origin(length,iteration):
    ittr = int(iteration)
    lens = int(length)
    origin=[]
    counter = ittr
    while counter > 0:
        pre_seq=rndn_sequence(lens)
        origin.extend(translate(pre_seq))
        counter -= 1
    # return getTable(origin)
    return origin

def generate_mutant(origin,base,locate,length):
    index = int(base)
    start = int(locate)
    end = int(length)
    mutate=[]
    for sequence in origin:
        pre_seq=one_flame_shift(sequence,index,start,end)
        mutate.extend(translate(pre_seq))
    # return getTable(mutate)
    return mutate

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
    read_seq = str(mRNA_seq)
    dic=[]
    if re.findall(r"AUG",read_seq) == []:
        dic.append({'STT':0,'STP':0,'LEN':0,'codon':'','protain':'','DNA':str(DNA_seq),'cDNA': str(cDNA_seq),'mRNA': read_seq})
    else:
        start = re.finditer(r"AUG",read_seq)
        for s in start:
            tmp=make_codon(read_seq,s.start())
            tmp.update({'DNA':str(DNA_seq),'cDNA': str(cDNA_seq),'mRNA': read_seq})
            dic.append(tmp)
    return dic

def make_codon(read_seq,start):
    pre_codon = read_seq[start:]
    pre_prot = read_codon(pre_codon)
    point = pre_prot.find(stop_str)
    stop = point
    if point+1>0:
        stop=start+point*3
    codon=pre_codon[:stop]
    prot=pre_prot[:point]
    return formatResult(start,stop,codon,prot)

def read_codon(pre_codon):
    codon=Seq(pre_codon, IUPAC.ambiguous_rna)
    result=codon.translate(stop_symbol=stop_str)
    return str(result)

def formatResult(start,stop,codon,prot,sep='-'):
    return {'STT':start+1,'STP':stop+1,'LEN':len(prot),'codon':codon,'protain':prot}