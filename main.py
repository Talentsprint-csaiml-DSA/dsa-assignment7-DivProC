def longest_common_subsequence(a, b):
    Pos = [[0 for x in range(len(b) + 1)] for y in range(len(a)+1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                Pos[i][j] = 1 + Pos[i-1][j-1]
            else:
                Pos[i][j] = max(Pos[i-1][j], Pos[i][j-1])
    return Pos[i][j]
               
