serine_codons = ("AGC", "AGU", "UCU", "UCC", "UCA", "UCG")

seq = "AUGUCCUCA"

for i in range(len(seq)-2):
    if seq[i:i+3] == "AUG":
        i += 3
        if seq[i:i+3] and seq[i+3:i+6] in serine_codons: # klammerninhalt mathematisch ausgedrückt: [i, n[ (wieso auch immer)
            print("yes") 
            break