def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        seqs = []
        current_seq = []
        
        for line in lines:
            if line.startswith(">"):  # Skip the header
                if current_seq:  # If we have a sequence in progress, save it
                    seqs.append("".join(current_seq))
                    current_seq = []  # Reset for the next sequence
            else:
                current_seq.append(line.strip())  # Collect sequence lines
        
        if current_seq:  # Append the last sequence after processing
            seqs.append("".join(current_seq))
            
        return seqs


def edit_dist(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases for DP table
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting all characters from s
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting all characters into s
    
    # Fill the DP table using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters match
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )
    
    # Traceback to get the aligned sequences
    aligned_s = []
    aligned_t = []
    
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s[i - 1] == t[j - 1]:
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or dp[i][j] == dp[i - 1][j] + 1):
            aligned_s.append(s[i - 1])
            aligned_t.append('-')  # Gap in t
            i -= 1
        elif j > 0 and (i == 0 or dp[i][j] == dp[i][j - 1] + 1):
            aligned_s.append('-')  # Gap in s
            aligned_t.append(t[j - 1])
            j -= 1
        else:
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1

    aligned_s.reverse()
    aligned_t.reverse()
    
    # Return the edit distance and aligned sequences
    return dp[m][n], ''.join(aligned_s), ''.join(aligned_t)


if __name__ == "__main__":
    input_filename = "input.txt"  # Input file containing the sequences
    seqs = read_fasta(input_filename)  # Read sequences from file
    
    if len(seqs) == 2:  # Check if exactly two sequences are found
        s = seqs[0]
        t = seqs[1]
        distance, aligned_s, aligned_t = edit_dist(s, t)  # Calculate the edit distance
        print(distance)  # Print the edit distance
        print(aligned_s)  # Print the aligned first sequence
        print(aligned_t)  # Print the aligned second sequence
    else:
        print("Error: The file should contain exactly two sequences in FASTA format.")
