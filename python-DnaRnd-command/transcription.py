import random

dna = ["A","G","C","T"]

def sequence(maximum):
    sequence=''
    for i in range(0,maximum):
        sequence+=random.choice(dna)
    return sequence

def complement(sequence):
    output = ''
    for letter in sequence:
        letter = letter.upper()
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        elif letter == 'C':
            output += 'G'
        else:
            output += ''
    return(output)

def messenger(sequence):
    output = ''
    for letter in sequence:
        letter = letter.upper()
        if letter == 'A':
            output += 'U'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        elif letter == 'C':
            output += 'G'
        else:
            output += ''
    return(output)
