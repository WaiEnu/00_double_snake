import transcription
import mutation
import translation

def sequence(input_max):
    range_max=int(input_max)
    sequence=transcription.sequence(range_max)
    return sequence

def mutate(sequence,base,locate,maximum):
    index = int(base)-1
    point = int(locate)
    end = int(maximum)
    out = mutation.one_flame_shift(sequence,index,point,end)
    return out

def out_seq(sequence):
    print('DNA[b]: ' + sequence)
    cDNA_sequence = transcription.complement(sequence)
    print('DNA[c]: ' + cDNA_sequence)
    mRNA_sequence = transcription.messenger(sequence)
    print('mRNA  : ' + mRNA_sequence)
    read_list=translation.translate(mRNA_sequence)
    print('codon : ' + read_list[0])
    print('prot  : ' + read_list[1])
    print('')
