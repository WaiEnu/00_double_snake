import detaset
import genetics

def generate_origin(length,iteration):
    ittr = int(iteration)
    lens = int(length)
    origin=[]
    for i in range(0,ittr):
        pre_seq=genetics.rndn_sequence(lens)
        origin.append(genetics.transcribe(pre_seq))
    dic = {'table':getTable(origin),'read':getReadable(origin)}
    return dic

def generate_mutant(origin,base,locate,length):
    index = int(base)
    start = int(locate)
    end = int(length)
    mutate=[]
    for sequence in origin:
        pre_seq=genetics.one_flame_shift(sequence,index,start,end)
        mutate.append(genetics.transcribe(pre_seq))
    dic = {'table':getTable(mutate),'read':getReadable(mutate)}
    return dic

def getTable(sequences):
    master=sequences
    master_DNA=detaset.getRow(master,'DNA')
    master_CNA=detaset.getRow(master,'cDNA')
    master_RNA=detaset.getRow(master,'mRNA')
    dic = {'DNA':master_DNA,'cDNA':master_CNA,'mRNA':master_RNA}
    return dic

def getReadable(sequences):
    master=[]
    for sequence in sequences:
        master.extend(genetics.translate(sequence['mRNA']))
    master_STT=detaset.getRow(master,'STT')
    master_STP=detaset.getRow(master,'STP')
    master_LEN=detaset.getRow(master,'LEN')
    master_COD=detaset.getRow(master,'codon')
    master_PRO=detaset.getRow(master,'protain')
    master_MRN=detaset.getRow(master,'mRNA')
    dic = {'STT':master_STT,'STP':master_STP,'LEN':master_LEN,'codon':master_COD,'protain':master_PRO,'mRNA':master_MRN}
    return dic