# # Copy your PatternCount function from the previous step below this line

def pattern_count(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    count = 0
    for i in range(text_len - pattern_len + 1):
        if(text[i : i + pattern_len] == pattern):
            count = count + 1
    return count


# # Now, we will set Text equal to the oriC of Vibrio cholerae and Pattern equal to "TGATCA"
# text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
# pattern = "TGATCA"

# # Finally, let's print the result of calling PatternCount on Text and Pattern.
# print(pattern_count(text, pattern))

#Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern not in freq:
            freq[Pattern] = 1
        else:
            freq[Pattern] = freq[Pattern] + 1
    # add another for loop here to range over each k-mer Pattern of text and increase freq[Pattern] by 1 each time
    return freq

def FrequentWords(Text, k):
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    list = []
    for patterns in freq:
        if(freq[patterns] == m):
            list.append(patterns)
    return list

# Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
# k = 10

# # Finally, let's print the result of calling FrequentWords on Text and Pattern.
# print(FrequentWords(Text, k))


def ReverseComplement(Pattern):   
    Pattern = Pattern[::-1]
    str = ""
    for letter in Pattern:
        if(letter == 'c'):
            str += 'g'
        elif(letter == 'g'):
            str += 'c'
        elif(letter == 'a'):
            str += 't'
        elif(letter == 't'):
            str += 'a'
        elif(letter == 'C'):
            str += 'G'
        elif(letter == 'G'):
            str += 'C'
        elif(letter == 'A'):
            str += 'T'
        elif(letter == 'T'):
            str += 'A'
    return str


# print(ReverseComplement("atgc"))

# fill in your PatternMatching() function along with any subroutines that you need.
# Copy your PatternMatching function below this line.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    gLen = len(Genome)
    pLen = len(Pattern)
    for i in range(gLen - pLen + 1):
        if(Genome[i:i+pLen] == Pattern):
            positions.append(i)
    return positions

# # Behind the scenes, we read in Genome equal to the genome of V. cholerae.
# with open("genome.txt", 'r') as file:
#     Genome = file.read()

# # Set Pattern equal to "CTTGATCAT"
# Pattern = "CTTGATCAT"

# # Call PatternMatching on Pattern and Genome, and store the output as a variable called positions
# positions = PatternMatching(Pattern, Genome)

# # print the positions variable
# print(positions)

# # On the following line, let's create a variable called Text that is equal to the oriC region from T petrophila

# # On the following line, let's create a variable called Text that is equal to the oriC region from T petrophila
# Text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"


# # On the following line, create a variable called count_1 that is equal to the number of times
# # that "ATGATCAAG" occurs in Text.
# count_1 = pattern_count(Text, "ATGATCAAG")

# # On the following line, create a variable called count_2 that is equal to the number of times
# # that "CTTGATCAT" occurs in Text. 
# count_2 = pattern_count(Text, "CTTGATCAT")


# # Finally, print the sum of count_1 and count_2
# print(count_1 + count_2)


print(pattern_count("ACTGTACGATGATGTGTGTCAAAG", "TGT"))
print(FrequentWords("CCGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA",3))
print(ReverseComplement( "GATTACA" ))