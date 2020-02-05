import const

const.amino_list = {
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
const.sep='-'
const.dna = ["A","G","C","T"]

def sep_str():
    return const.sep

def sepN_str():
    return ''

def dna():
    return const.dna

def amino():
    return const.amino_list