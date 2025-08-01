# Overlap Graphs

# A Brief Introduction to Graph Theory

# Problem
# A graph whose nodes have all been labeled can be represented by an adjacency list,
# in which each row of the list contains the two node labels corresponding to a unique edge.

# A directed graph (or digraph) is a graph containing directed edges,
# each of which has an orientation.
# That is, a directed edge is represented by an arrow instead of a line segment;
# the starting and ending nodes of an edge form its tail and head, respectively.
# The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)).
# A directed loop is a directed edge of the form (v,v).

# For a collection of strings and a positive integer k,
# the overlap graph for the strings is a directed graph Ok in which each string is represented by a node,
# and string s is connected to string t with a directed edge when there is a length k suffix of s
# that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops
# in the overlap graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length
# at most 10 kbp.

# Return: The adjacency list corresponding to O3.
# You may return edges in any order.

# Sample Dataset

# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG

# Sample Output

# Rosalind_0498 Rosalind_2391
# Rosalind_0498 Rosalind_0442
# Rosalind_2391 Rosalind_2323

# 너무 어렵다...

current_id = ""
current_sequences_parts = []
fasta_records = {}  # ID: 서열 딕셔너리

input_file_name = "/Users/s.w.jung/Downloads/바이오 관련/바이오 빅데이터 분석 교육 과정/정서우의 백준 도전기/0730 로잘린/rosalind_grph.txt"

with open(input_file_name, "r") as file_handle:
    for line in file_handle:
        cleaned_line = line.strip()

        if cleaned_line.startswith(">"):
            # 이전 레코드가 있다면 (첫 번째 '>'가 아닐 경우) 처리
            if current_id != "":
                fasta_records[current_id] = "".join(current_sequences_parts)

            # 새로운 레코드의 ID를 저장하고, 현재 서열을 초기화
            current_id = cleaned_line[1:]  # '>' 제외하고 ID 추출
            current_sequences_parts = []  # 새로운 서열을 모을 리스트 초기화
        else:
            # 서열 줄이면 현재 서열 리스트에 추가
            current_sequences_parts.append(cleaned_line)

# 파일의 모든 줄을 읽은 후, 마지막 FASTA 레코드를 처리 (중요!)
if current_id != "":
    fasta_records[current_id] = "".join(current_sequences_parts)

# --- 이제 fasta_records 딕셔너리에 모든 ID와 서열이 저장됨 ---

# 오버랩 엣지 찾기 (k=3)
k = 3  # 문제에서 k=3이라고 명시되어 있음

for id_s, seq_s in fasta_records.items():
    for id_t, seq_t in fasta_records.items():
        # 자기 자신과는 비교하지 않음 (s ≠ t 조건)
        if id_s == id_t:
            continue

        # s의 접미사(suffix) k글자와 t의 접두사(prefix) k글자 추출
        # 문자열 길이가 k보다 짧으면 오류가 날 수 있으나, 문제 조건상 1kbp라 충분히 김.
        s_suffix = seq_s[-k:]
        t_prefix = seq_t[0:k]

        # 오버랩 조건 확인 (접미사와 접두사가 같은지)
        if s_suffix == t_prefix:
            print(id_s, id_t)
