# Working with Files solved by 26378

# Problem
# Given: A file containing at most 1000 lines.

# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# Sample Dataset

# Bravely bold Sir Robin rode forth from Camelot
# Yes, brave Sir Robin turned about
# He was not afraid to die, O brave Sir Robin
# And gallantly he chickened out
# He was not at all afraid to be killed in nasty ways
# Bravely talking to his feet
# Brave, brave, brave, brave Sir Robin
# He beat a very brave retreat

# Sample Output

# Yes, brave Sir Robin turned about
# And gallantly he chickened out
# Bravely talking to his feet
# He beat a very brave retreat

input_filename = "rosalind_ini5.txt"

with open(input_filename, "r") as input_filename2:
    all_lines = input_filename2.readlines()

even_lines = []

for i in range(1, len(all_lines), 2):
    even_lines.append(all_lines[i])

output_filename = "output.txt"

with open(output_filename, "w") as output_file:
    output_file.writelines(even_lines)
