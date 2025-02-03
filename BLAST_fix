import random

base = ["A", "T", "G", "C"]

def generate_sequence(k):
    sequence = ""
    for i in range(0, k):
        nuc = random.randint(0, 3)
        sequence = sequence + base[nuc]
    return sequence


primer = generate_sequence(8)
print("Primer:", primer)
dna = generate_sequence(200000)
print("DNA:", dna)


def translate_primer(primer):
    t_primer = ""
    dic = {"A":"T", "T":"A", "G":"C", "C":"G"}
    for i in primer:
       t_primer = t_primer + dic[i]
    return t_primer

t_primer = translate_primer(primer)
print("t_primer:", t_primer)


for i in range(0, len(dna) - len(primer) + 1):  # Ensure we don't go out of bounds
    n = 0
    p = i
    if dna[i] == t_primer[0]:
        while p < len(dna) and n < len(primer) and dna[p] == t_primer[n]: # this got fixed
            n += 1
            p += 1
        if n == len(primer):  # If we matched the entire primer sequence # this also got fixed
            print(f"Match found at index {i-1}")
