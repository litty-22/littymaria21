def sub_ind(s, t):
    ind = []  
    t_inx = 0  
    n, m = len(s), len(t)
    for i in range(n):
        if s[i] == t[t_inx]: 
            ind.append(i + 1)  
            t_inx += 1 
        if t_inx == m: 
            break
    if len(ind) == m:
        return ind
    else:
        return []

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    seq = []
    cur_seq = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'): 
            if cur_seq:
                seq.append(''.join(cur_seq))
            cur_seq = []
        else:
            cur_seq.append(line)
    if cur_seq:
        seq.append(''.join(cur_seq))
    return seq[0], seq[1]

def main():
    filename = 'input.txt'  
    s, t = read_input(filename)
    result = sub_ind(s, t)
    if result:
        print(" ".join(map(str, result)))  
main()
