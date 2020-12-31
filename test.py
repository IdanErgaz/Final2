def solution(A):
    # write your code in Python 3.6
    mx = max(A)
    if mx< 1:
       return 1

    A = set(A)
    B = set(range(1, mx + 1))
    D = B - A
    print("D:", D)
    print(A)
    print(B)
    if len(D) == 0:
        return mx + 1
    else:
        return min(D)


A=[-1, 3, -6, 4, 1, 2]
solution(A)