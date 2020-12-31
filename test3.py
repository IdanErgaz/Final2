# def solution(N):
#     N=str(N)
#     m= max(N)
#     print("Max", m)
#
#     first=N.pop
#     last= N.pop-1
#     print(first)
#     print(last)
#     # int(str(n) + str(d))
#     for i in N:
#         print(str(i))


#     ar solution = function (N) {
#   let max = Number.MIN_SAFE_INTEGER;
#   for (let i = N >= 0 ? 0 : 1; i < `${N}`.length + 1; i++) {
#     const result = [`${N}`.slice(0, i), '5', `${N}`.slice(i)].join('');
#     console.log(result);
#     if (Number(result) > max) {
#       max = Number(result);
#     }
#   }
#   return max;
# };
#     :param N:
#     :return:
#     '''
#
# # solution(526)
#
# # numbers=str(123)
# # for i in numbers:
# #     print(i)
def solution(N):

    N=str(N)
    opt1 = N + "5"
    opt2 = "5" + N
    if "-" in N:
        return (min (abs(opt1, opt2)))
    else:
        print(opt1)
        print(opt2)
        return(max(opt1, opt2))


# solution(-23)
print(solution(85))
# if(opt1>opt2):
#     return (opt1)
# else:
#     return opt2999