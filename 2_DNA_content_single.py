# calculate the nucleotide content in a DNA sequence! (in percent) 
# calculating for multiple nucleotides is currently not supported

sequence = 'ATGCGCCTGAAC'
nuc = 1

nucleotide = ['A' = 0, 'T' = 0, 'G' = 0, 'C' =  0] 
n = 0

for i in sequence: # so inefficient but idk how to fix it
    if sequence[n] == 'A' :
        nucleotide[0] += 1

    elif sequence[n] == 'T' :
        nucleotide[1] += 1

    elif sequence[n] == 'G' :
        nucleotide[2] += 1

    elif sequence[n] == 'C' :
        nucleotide[3] += 1

    n +=1 


def content(type) :
    percentage = nucleotide[type] * 100 / len(sequence)
    return percentage

print(f"Input: \n  > Sequence: {sequence}, length: {len(sequence)} \n  > Selected nucleotide: {nuc} \n")

print(f"The selected nucleotide content of this sequence is {round(content(nuc), 1)}%.") 