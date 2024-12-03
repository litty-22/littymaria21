#PROGRAM 1 LGIS

def inc_sub(arr):
    n = len(arr)
    dp = [1] * n  
    par = [-1] * n  
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                par[i] = j
    
    is_len = max(dp)
    is_in = dp.index(is_len)
    lis = []
    while is_in != -1:
        lis.append(arr[is_in])
        is_in = par[is_in]

    lis.reverse()  
    return lis

def dec_sub(arr):
    arr_rev = arr[::-1]
    lis_rev = inc_sub(arr_rev)
    return lis_rev[::-1]  
def main():
    input_filename = 'input.txt'
    
    with open(input_filename, 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    lis = inc_sub(arr)
    lds = dec_sub(arr)
    print(' '.join(map(str, lis)))
    print(' '.join(map(str, lds)))
main()
