def solution(D, S):
    if S.casefold() == "one".casefold():
        return D*1
    elif S.casefold()=="two".casefold():
        return D*2
    elif S.casefold()=="three".casefold():
        return D*3
    elif S.casefold()=="four".casefold():
        return D*4
    elif S.casefold()=="five".casefold():
        return D* 5
    else:
        print("Unfamilier input please try again")

    # return D*int(S)




#Main:
# D=range(1, 6)
# S=["One", "Two", "Three", "Four", "Five"]



mix={"One":"", "Two":"", "Three":"", "Four":"", "Five":""}
print(solution(3, "ThrEE"))