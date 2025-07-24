# Identifying Unknown DNA Quickly

# Problem
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# Sample Dataset
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# Sample Output
# Rosalind_0808
# 60.919540


def calculate_gc_content(sequence):
    if not sequence:
        return 0.0

    gc_count = sequence.count("C") + sequence.count("G")
    total_bases = len(sequence)
    return (gc_count / total_bases) * 100


def solve_rosalind_gc(filename):
    fasta_records = {}

    current_id = None
    current_sequence_parts = []

    with open("rosalind_gc.txt", "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if current_id is not None:
                    fasta_records[current_id] = "".join(current_sequence_parts)

                current_id = line[1:]
                current_sequence_parts = []
            else:
                current_sequence_parts.append(line)

    if current_id is not None:
        fasta_records[current_id] = "".join(current_sequence_parts)

    max_gc_value = -1.0
    best_id = ""

    for record_id, dna_sequence in fasta_records.items():
        current_gc = calculate_gc_content(dna_sequence)

        if current_gc > max_gc_value:
            max_gc_value = current_gc
            best_id = record_id

    return best_id, max_gc_value


file_name = "rosalind_gc.txt"
highest_gc_id, highest_gc_content = solve_rosalind_gc(file_name)

print(highest_gc_id)
print(f"{highest_gc_content:.6f}")
