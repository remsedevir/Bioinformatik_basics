# "alledged weird bioinformatics question made by chatgpt"

sequence = "" # insert dna here

base = {"A":"T", "T":"A", "G":"C", "C":"G"}

def reverse_sequence(sequence):
    r_sequence = ""
    for i in sequence:
        r_sequence += base[i]
    return r_sequence

reversed = reverse_sequence(sequence)

if sequence == reversed[::-1]: # remember this, very cool
    print("The given sequence is palindromic.")
        
else:
    print("The given sequence is not palindromic.")
    

