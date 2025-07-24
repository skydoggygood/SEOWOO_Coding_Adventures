# A_Rapid_Introduction_to_Molecular_Biology

# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s
#  of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
# .

# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 20 12 17 21

# 정서우 제출 코드

s = input()

bases_count = {"A":0, "C":0, "G":0, "T":0}

for i in s :
    if "A" in s : # 이건 s에 A가 있냐 없냐를 계속 확인하는 것이기에 의미가 없음 (이건 문자를 계속 돌면서 계속 검사하기 때문에 아래 코드들 역시 무의미한 코드들임)
        bases_count[i] += 1  
    elif "C" in s :
        bases_count[i] += 1
    elif "G" in s :
        bases_count[i] += 1
    elif "T" in s :
        bases_count[i] += 1

for i,count in bases_count.items():
    print(count, end=" ")

# 내 코드는 모든 입력값이 ATCG로 구성되어 있고, 중간에 N 같은게 섞여있었다면 오류가 떴을 거임

# 문제 입력값 
# TTCTAGATTCAACAGTGAAATTTAGCGGAAGAACTATGCGGTAACGCGGGGTTAATTCATCTTTTACGTGCACCGGTCATGAAAAAGCCGACGAATGTCGTGTACGCCTGATAATCTTTGCATCCTGTAGTTTTTAATGGTGCGAGCGGCGGTCGTCGCGGTCCATGGTGCGTCCCATTGTATCTAGTCGATACTCATTAGAAAGCCATGGGCCAGGTGCTAAGCGACCAGAAACAACTTGCTGTCTATTAGGAAAGCAAAACGCCCCGGGAGCGTACCTCTAACGCGTTAGCACGCTCTGGGCCAGAGCTTACGAGAGATACGCCAAGATTCAATTAATGGCATTGTAAGTTCTTCCGCAAGAATAAGGCTGAAATCTAGGCCAGCGTCGGGTGCTAAACCAGATTTGTAGAATGCTTCTCCGTGACTTACTAGGGCCAAAGACCTGCTATCGCTAAATACGGGTCATGTGTCTACTCTTGATGGTCTGAAGGCTCGGTCGACCGTGCCCACTAGAGGAGGCAAGCTGAATTGCGGACTACGAACCGGAAGTCCCGAAGTGCTAGAGAAGACGTTAATTCGCGAGCCCTGTCTATGCGTCTTTCCGCTGAGGAGCGGTGAGAAATAAGAATCGATCTGAACCGGCCTAGTGGCTGCTGTAGTACCCAGTACGGTAATGTGATGAAAGCACTGAGGTCCAAGATAGACCAACGGAGTCAAGCGTTCGAGGGGCTACTGCTCGTAGAAGACTTCTGGCAATCACTGGGTTGTTGCAAGTGTCCGAGCCGCTGGTGTTTATTGCGAAAATCGCTTGAGTTACCTGCGCTGTATTAAATATTTCTGTTGTTAGCGCAAGGCCCCGAGCGGGTTAAGAGTCTAAATTTAGCGTCGACGTGCCGTTTGAAATGAGTAACAAGACACATTAAAATACTAACCCAAGCCGATTTTATA
# 문제 정답
# 250 211 253 237

# CHAT GPT 코드 

# s = input()
# bases_count = {"A":0, "C":0, "G":0, "T":0}

# for base in s :
#     if base in bases_count :
#         bases_count[base] += 1

# print(bases_count["A"],bases_count["C"],bases_count["G"],bases_count["T"])