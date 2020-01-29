
dna = ["A","G","C","T"]

def one_flame_shift(sequence,index,point,end):
    out_before = sequence[0:point]
    out_after = sequence[point:end]
    out=out_before+dna[index]+out_after
    return out