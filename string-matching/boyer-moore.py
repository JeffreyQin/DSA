

VOCAB_SIZE = 127

def compute_last_occurrence(P):

    last_occur_arr = [-1] * VOCAB_SIZE
    for i in range(len(P)):
        last_occur_arr[ord(P[i])] = i

    return last_occur_arr
    

def bad_char_heuristic(T, P):

    last_occur_arr = compute_last_occurrence(P)

    n = len(T)
    m = len(P)

    i = 0
    while i <= n - m:
        j = m - 1

        while j >= 0 and P[j] == T[i + j]:
            j -= 1
        
        if j == -1:
            return "FOUND AT " + str(i)
        else:
            i += max(1, j - last_occur_arr[ord(T[i + j])])

    return "NOT FOUND"




if __name__ == "__main__":

    T = "ABAAAABCD"
    P = "ABC"

    result = bad_char_heuristic(T, P)
    print(result)