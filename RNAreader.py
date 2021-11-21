inputfile ="rosalind_rna(1).txt"
f = open(inputfile, "r")
seq = f.read()
rnaseq = seq.replace('T','U')
print(rnaseq)