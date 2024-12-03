def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        seqs = []
        cur_seq = []
        for l in lines:
            if l.startswith(">"):  
                if cur_seq:  
                    seqs.append("".join(cur_seq))
                    cur_seq = []  
            else:
                cur_seq.append(l.strip()) 
        if cur_seq: 
            seqs.append("".join(cur_seq))
        return seqs

def edit_dist(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i 
    for j in range(n + 1):
        dp[0][j] = j  
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] 
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )
    
    return dp[m][n]

if __name__ == "__main__":
    input_filename = "input.txt"  
    seqs = read_fasta(input_filename)  
    
    if len(seqs) == 2:  
        s = seqs[0]
        t = seqs[1]
        result = edit_dist(s, t)  
        print(result) 