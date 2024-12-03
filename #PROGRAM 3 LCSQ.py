def com_sub(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            lcs.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    seqs = []
    seq = ''
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if seq:
                seqs.append(seq)
            seq = ''
        else:
            seq += line
    
    if seq:
        seqs.append(seq)

    return seqs
input_file = 'input.txt' 
seqs = read_fasta(input_file)
s = seqs[0]
t = seqs[1]
result = com_sub(s, t)
print(result)
