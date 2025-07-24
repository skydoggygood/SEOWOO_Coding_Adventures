# 25206번

# 문제
# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!

# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

# 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.

# A+	4.5
# A0	4.0
# B+	3.5
# B0	3.0
# C+	2.5
# C0	2.0
# D+	1.5
# D0	1.0
# F	0.0
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.

# 과연 치훈이는 무사히 졸업할 수 있을까?

# 입력
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

# 출력
# 치훈이의 전공평점을 출력한다.

# 정답과의 절대오차 또는 상대오차가
# \(10^{-4}\) 이하이면 정답으로 인정한다.

# 제한
# 1 ≤ 과목명의 길이 ≤ 50
# 과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
# 학점은 1.0,2.0,3.0,4.0중 하나이다.
# 등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
# 적어도 한 과목은 등급이 P가 아님이 보장된다.
# 예제 입력 1
# ObjectOrientedProgramming1 3.0 A+
# IntroductiontoComputerEngineering 3.0 A+
# ObjectOrientedProgramming2 3.0 A0
# CreativeComputerEngineeringDesign 3.0 A+
# AssemblyLanguage 3.0 A+
# InternetProgramming 3.0 B0
# ApplicationProgramminginJava 3.0 A0
# SystemProgramming 3.0 B0
# OperatingSystem 3.0 B0
# WirelessCommunicationsandNetworking 3.0 C+
# LogicCircuits 3.0 B0
# DataStructure 4.0 A+
# MicroprocessorApplication 3.0 B+
# EmbeddedSoftware 3.0 C0
# ComputerSecurity 3.0 D+
# Database 3.0 C+
# Algorithm 3.0 B0
# CapstoneDesigninCSE 3.0 B+
# CompilerDesign 3.0 D0
# ProblemSolving 4.0 P
# 예제 출력 1
# 3.284483
# 예제 입력 2
# BruteForce 3.0 F
# Greedy 1.0 F
# DivideandConquer 2.0 F
# DynamicProgramming 3.0 F
# DepthFirstSearch 4.0 F
# BreadthFirstSearch 3.0 F
# ShortestPath 4.0 F
# DisjointSet 2.0 F
# MinimumSpanningTree 2.0 F
# TopologicalSorting 1.0 F
# LeastCommonAncestor 2.0 F
# SegmentTree 4.0 F
# EulerTourTechnique 3.0 F
# StronglyConnectedComponent 2.0 F
# BipartiteMatching 2.0 F
# MaximumFlowProblem 3.0 F
# SuffixArray 1.0 F
# HeavyLightDecomposition 4.0 F
# CentroidDecomposition 3.0 F
# SplayTree 1.0 F
# 예제 출력 2
# 0.000000

major_score = [input() for i in range(20)]

major_grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

sum_score = 0
total_credit = 0

for _ in range(len(major_score)):
    major_score_detail = major_score[_].split(" ")
    if major_score_detail[2] == "P":
        continue
    else:
        conversion_score = major_grade.get(major_score_detail[2])
        sum_score += conversion_score * float(major_score_detail[1])
        total_credit += float(major_score_detail[1])

final_major_grade = sum_score / total_credit

print(round(final_major_grade, 6))


# 입력값을 여러 줄 한번에 받기 (성공)
# 입력값을 리스트로 처리하고, 리스트 내부 [1]과 [2]를 따로 출력 (성공)
# [2]는 전공등급이므로 이를 점수로 환산 예) A+ -> 4.5 로 (성공)
# 환산한 점수와 [1] (학점) 을 곱해서 계산 (성공)
# 이들 모두의 합산을 구함 / 이 과정에서 학점의 총합도 미리 구해두기 (성공)
# 전공평점 = sum(학점 * 과목평점) / (학점의 총합)
# 만약 P인 과목이 있다면 이건 계산에서 제외 / F 는 0점 (성공)
