import random

base = ["A", "T", "G", "C"]
#primer = "TAT"

# nuc = random.randint(0,3) # wichtig!!

def generate_sequence(k):
    sequence = ""
    for i in range (0,k):
        nuc = random.randint(0,3)
        sequence = sequence + base[nuc]
    return sequence


#dna = generate_sequence() # spart Schreibaufwand, sorgt dafür, dass wir hier nicht aus Versehen eine neue Sequenz bilden 
primer = generate_sequence(2)
print(primer)
dna = generate_sequence(200)
print(dna)


for i in range(0,len(dna)-len(primer)):   
    n = 0
    p = 0
    if dna[i] == primer[0]:
        p = i + 1
        n += 1
        while dna[p] == primer[n]: # idk why that's not working
            n += 1
            p += 1
            if n == len(primer):
                break
        if dna[p] == primer[-1]:
            print(i)
