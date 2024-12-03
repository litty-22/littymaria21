MOD = 134217727

def num_alignments(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    count = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
        count[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = j
        count[0][j] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            min_cost = min(dp[i - 1][j - 1] + cost, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            dp[i][j] = min_cost
            if dp[i - 1][j - 1] + cost == min_cost:
                count[i][j] += count[i - 1][j - 1]
            if dp[i - 1][j] + 1 == min_cost:
                count[i][j] += count[i - 1][j]
            if dp[i][j - 1] + 1 == min_cost:
                count[i][j] += count[i][j - 1]
            count[i][j] %= MOD
    
    return count[m][n]

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        seqs = []
        seq = ""
        
        for l in lines:
            l = l.strip()
            if l.startswith('>'):
                if seq:
                    seqs.append(seq)
                seq = ""
            else:
                seq += l
        seqs.append(seq)  
        
        return seqs

def main():
    file_path = 'input.txt'  
    seqs = read_from_file(file_path)
    if len(seqs) != 2:
        print("Error")
        return
    
    s = seqs[0]
    t = seqs[1]
    result = num_alignments(s, t)
    print(result)

if __name__ == "__main__":
    main()
