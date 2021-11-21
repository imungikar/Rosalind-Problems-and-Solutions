inputfile = "rosalind_revc(1).txt"
f = open(inputfile, "r")
oseq = f.read()
seq = oseq[::-1]
for base in seq:
    if base =="A":
        seq.replace('A','T')
    if base=="T":
        seq.replace('T','A')
    if base=="G":
        seq.replace('G','C')
    if base=="C":
        seq.replace('C','G')

print(seq)