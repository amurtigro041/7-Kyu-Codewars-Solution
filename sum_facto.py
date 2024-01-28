def sum_facto(list):
    import numpy as np
    result_lst = []
    facto_lst = []
    for i in range(0,len(list)):
        if list[i] == 1:
            result_lst.append(1)
        else:
            for integer in range(1,list[i] + 1):
                facto_lst.append(integer)
            factorial = np.prod(facto_lst)
            result_lst.append(factorial)
            facto_lst.clear()

    result = np.sum(result_lst)
    return result
print(sum_facto([4,6]))
print(sum_facto([3,2]))