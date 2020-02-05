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
    master_STT=getRow(master,'STT')
    master_STP=getRow(master,'STP')
    master_LEN=getRow(master,'LEN')
    master_COD=getRow(master,'codon')
    master_PRO=getRow(master,'protain')
    master_DNA=getRow(master,'DNA')
    master_CNA=getRow(master,'cDNA')
    master_RNA=getRow(master,'mRNA')
    dic = {'STT':master_STT,'STP':master_STP,'LEN':master_LEN,'codon':master_COD,'protain':master_PRO,'DNA':master_DNA,'cDNA':master_CNA,'mRNA':master_RNA}
    return dic

def getRow(dic,str_obj):
    arr = [d.get(str_obj) for d in dic]
    return arr