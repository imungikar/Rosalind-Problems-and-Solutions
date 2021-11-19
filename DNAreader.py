inputfile ="rosalind_dna.txt"
f = open(inputfile, "r")
seq = f.read()
a = 0
g = 0
c = 0
t = 0
for base in seq:
    if base == "A":
        a += 1
    elif base == "C":
        c += 1
    elif base == "G":
        g += 1
    elif base == "T":
        t += 1
print(str(a)+' '+str(c)+' '+ str(g)+ ' '+str(t))