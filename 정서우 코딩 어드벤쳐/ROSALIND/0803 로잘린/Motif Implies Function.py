# Motif Implies Function

# Problem
# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

# You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

# http://www.uniprot.org/uniprot/uniprot_id
# Alternatively, you can obtain a protein sequence in FASTA format by following

# http://www.uniprot.org/uniprot/uniprot_id.fasta
# For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

# Given: At most 15 UniProt Protein Database access IDs.

# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

# Sample Dataset
# A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST
# Sample Output
# B5ZC00
# 85 118 142 306 395
# P07204_TRBM_HUMAN
# 47 115 116 382 409
# P20840_SAG1_YEAST
# 79 109 135 248 306 348 364 402 485 501 614

import requests
import re

import requests

def get_fasta_sequence(uniprot_id):
    # accession만 추출
    acc = uniprot_id.split('_')[0]
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    res = requests.get(url)
    data = res.text.strip().split('\n')
    return ''.join(data[1:]).replace('\n', '').replace('\r', '')

def find_motif(seq):
    positions = []
    for i in range(len(seq) - 3):
        if (
            seq[i] == 'N' and
            seq[i+1] != 'P' and
            seq[i+2] in ['S', 'T'] and
            seq[i+3] != 'P'
        ):
            positions.append(i + 1)  # 1-based
    return positions

def main():
    with open("rosalind_mprt.txt") as f:
        ids = [line.strip() for line in f if line.strip()]
    for uid in ids:
        seq = get_fasta_sequence(uid)
        motif_pos = find_motif(seq)
        if motif_pos:
            print(uid)
            print(' '.join(map(str, motif_pos)))

if __name__ == "__main__":
    main()