def pattern_count(pattern, text):
    text_len = len(text)
    pattern_len = len(pattern)
    count = 0
    for i in range(text_len - pattern_len + 1):
        if(text[i : i + pattern_len] == pattern):
            count = count + 1
    return count

def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2]

    array[0] = pattern_count(symbol, extended_genome[0:n//2])

    for i in range(1,n):
        array[i] = array[i-1]
        if(extended_genome[i-1]==symbol):
            array[i] -= 1
        if(extended_genome[i+n//2-1]==symbol):
            array[i] += 1
    return array

def skew_array(genome):
    arr = []
    arr.append(0)
    for i in range(len(genome)):
        if(genome[i] == 'G'):
            arr.append(arr[i] + 1)
        elif(genome[i] == 'C'):
            arr.append(arr[i] - 1)
        else:
            arr.append(arr[i])
    return arr
            
with open("ecoli.txt", "r") as file:
    ecoli = file.read()
print(skew_array(ecoli))
