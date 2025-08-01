# Finding a Shared Motif

# Searching Through the Haystack

# Problem
# A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# Sample Dataset

# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA

# Sample Output

# AC

# current_id = ""
# current_sequences_parts = []
# fasta_records = {}

# input_file_name = "/Users/s.w.jung/Downloads/바이오 관련/바이오 빅데이터 분석 교육 과정/정서우의 백준 도전기/8월/0801 로잘린/rosalind_lcsm.txt"  # 아직 안정해짐

# with open(input_file_name, "r") as file_handle:
#     for line in file_handle:
#         cleaned_line = line.strip()

#         if cleaned_line.startswith(">"):
#             if current_id != "":
#                 fasta_records[current_id] = "".join(current_sequences_parts)
#             current_id = cleaned_line[1:]
#             current_sequences_parts = []
#         else:
#             current_sequences_parts.append(cleaned_line)

# if current_id != "":
#     fasta_records[current_id] = "".join(current_sequences_parts)

# sequences = list(fasta_records.values())

# short_seq_len = min(len(s) for s in sequences)

# for length in range(short_seq_len, 0, -1):
#     first_sequence = sequences[0]
#     for i in range(len(first_sequence) - length + 1):
#         substring = first_sequence[i : i + length]

#         is_common = True

#         for other_sequence in sequences[1:]:
#             if substring not in other_sequence:
#                 is_common = False
#                 break

#         if is_common:
#             print(substring)
#             exit()

current_id = ""
current_sequences_parts = []
fasta_records = {}

input_file_name = "/Users/s.w.jung/Downloads/바이오 관련/바이오 빅데이터 분석 교육 과정/정서우의 백준 도전기/8월/0801 로잘린/test.txt"  # 아직 안정해짐

with open(input_file_name, "r") as file_handle:
    for line in file_handle:
        cleaned_line = line.strip()

        if cleaned_line.startswith(">"):
            if current_id != "":
                fasta_records[current_id] = "".join(current_sequences_parts)
            current_id = cleaned_line[1:]
            current_sequences_parts = []
        else:
            current_sequences_parts.append(cleaned_line)

if current_id != "":
    fasta_records[current_id] = "".join(current_sequences_parts)

sequences = list(fasta_records.values())

min_sequences = min(sequences, key=len)

all_substrings = set()

for i in range(len(min_sequences)):
    for j in range(i + 1, len(min_sequences) + 1):
        substring = min_sequences[i:j]
        if len(substring) > 1:
            all_substrings.add(substring)

other_sequences = [s for s in sequences if s != min_sequences]

to_remove = set()

for seq in other_sequences:
    for substrings in all_substrings:
        if substrings not in seq:
            to_remove.add(substrings)

    all_substrings = all_substrings - to_remove

if all_substrings:
    max_length = max(len(s) for s in all_substrings)

    for s in all_substrings:
        if len(s) == max_length:
            print(s)
            break
