import detaset
import genetics

def generate_origin(length,iteration):
    ittr = int(iteration)
    lens = int(length)
    origin=[]
    for i in range(0,ittr):
        pre_seq=genetics.rndn_sequence(lens)
        origin.extend(genetics.translate(pre_seq))
    dic = getTable(origin)
    return dic

def generate_mutant(origin,base,locate,length):
    index = int(base)
    start = int(locate)
    end = int(length)
    mutate=[]
    for sequence in origin:
        pre_seq=genetics.one_flame_shift(sequence,index,start,end)
        mutate.extend(genetics.translate(pre_seq))
    dic = getTable(mutate)
    return dic

def getTable(master):
    master_STT=detaset.getRow(master,'STT')
    master_STP=detaset.getRow(master,'STP')
    master_LEN=detaset.getRow(master,'LEN')
    master_COD=detaset.getRow(master,'codon')
    master_PRO=detaset.getRow(master,'protain')
    master_DNA=detaset.getRow(master,'DNA')
    master_CNA=detaset.getRow(master,'cDNA')
    master_RNA=detaset.getRow(master,'mRNA')
    dic = {'STT':master_STT,'STP':master_STP,'LEN':master_LEN,'codon':master_COD,'protain':master_PRO,'DNA':master_DNA,'cDNA':master_CNA,'mRNA':master_RNA}
    return dic