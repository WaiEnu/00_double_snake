import genetics

def generate_origin(length,iteration):
    ittr = int(iteration)
    lens = int(length)
    origin=[]
    counter = ittr
    while counter > 0:
        pre_seq=genetics.rndn_sequence(lens)
        origin.extend(genetics.translate(pre_seq))
        counter -= 1
    return getTable(origin)

def generate_mutant(origin,base,locate,length):
    index = int(base)
    start = int(locate)
    end = int(length)
    mutate=[]
    for sequence in origin:
        pre_seq=genetics.one_flame_shift(sequence,index,start,end)
        mutate.extend(genetics.translate(pre_seq))
    return getTable(mutate)

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