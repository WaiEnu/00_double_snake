amino_list = {
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
sep='-'

def translate(seq):
    result=[]
    codon=make_codon(seq)
    prot=read_codon(codon)
    result.append(sep.join(codon))
    result.append(sep.join(prot))
    return result

def make_codon(read_seq,k=3):
    result=[]
    start = read_seq.find("AUG")
    pre_codon = read_seq[start::]
    result.append(str(start))
    for i in range(0, len(pre_codon), k):
        codon = pre_codon[i:i+k]
        if codon in amino_list["x"]:
            #result.append(codon)
            result.append(str(start+i))
            return result
        elif len(codon)<3 :
            result.append(str(start+i))
            return result
        else:
            result.append(codon)
    return result

def read_codon(codon_list):
    result =[]
    for i in range(0,len(codon_list)):
        aminosan=codon_list[i]
        aminosan_check = [k for k, v in amino_list.items() if codon_list[i] in v]
        if len(aminosan_check) != 0:
            aminosan = aminosan_check[0]
        result.append(aminosan)
    return result
