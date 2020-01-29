import detaset

dna=detaset.dna()
dna_len=len(dna)

def one_flame_shift(sequence,index,point,end):
    out_before = sequence[0:point-1]
    out_after = sequence[point:end-1]
    out=''
    if(index < dna_len):
        out = out_before + dna[index-1] + out_after
    else:
        out = out_before[:-1] + out_after
    return out