# Finding a Most Likely Common Ancestor

# Problem
# A matrix is a rectangular table of values divided into rows and columns.
# An m × n matrix has m rows and n columns.
# Given a matrix A , we write Ai,j to indicate the value found at the intersection of row i and column j.

# Say that we have a collection of DNA strings,
# all having the same length n.
# Their profile matrix is a 4×n matrix P in which P1,
# j represents the number of times that 'A' occurs in the jth position of one of the strings,
# P2,j represents the number of times that C occurs in the jth position,
# and so on (see below).

# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position;
# the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course,
# there may be more than one most common symbol,
# leading to multiple possible consensus strings.

# DNA Strings

# A T C C A G C T
# G G G C A A C T
# A T G G A T C T
# A A G C A A C C
# T T G G A A C T
# A T G C C A T T
# A T G G C A C T

# Profile

# A   5 1 0 0 5 5 0 0
# C   0 0 1 4 2 0 6 1
# G   1 1 6 3 0 1 0 0
# T   1 5 0 0 0 1 1 6

# Consensus	A T G C A A C T

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# Sample Dataset

# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT

# Sample Output

# ATGCAACT

# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6


def parse_fasta(file_path):
    dna_sequences = []
    current_dna = ""

    try:
        with open(file_path, "r") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line.startswith(">"):
                    if current_dna:
                        dna_sequences.append(current_dna)
                    current_dna = ""
                else:
                    current_dna += cleaned_line

            if current_dna:
                dna_sequences.append(current_dna)
        return dna_sequences
    except FileNotFoundError:
        return []


file_path = "rosalind_cons.txt"
fasta_parse = parse_fasta(file_path)
lines_list = []

if fasta_parse:
    for line in fasta_parse:
        lines = line.strip()
        lines_list.append(lines)

sequence_length = len(lines_list[0])

profile = [[0] * sequence_length for _ in range(4)]

for i in range(sequence_length):
    for dna_seq in lines_list:
        if dna_seq[i] == "A":
            profile[0][i] += 1
        if dna_seq[i] == "C":
            profile[1][i] += 1
        if dna_seq[i] == "G":
            profile[2][i] += 1
        if dna_seq[i] == "T":
            profile[3][i] += 1

consensus = []

for k in range(sequence_length):
    current_counts = profile[0][k], profile[1][k], profile[2][k], profile[3][k]
    V = max(current_counts)
    Z = current_counts.index(V)
    if Z == 0:
        Z = "A"
    elif Z == 1:
        Z = "C"
    elif Z == 2:
        Z = "G"
    elif Z == 3:
        Z = "T"
    consensus.append(Z)

bases = ["A", "C", "G", "T"]

print("".join(consensus))

for l in range(4):
    counts_str = " ".join(map(str, profile[l]))
    print(f"{bases[l]}: {counts_str}")
