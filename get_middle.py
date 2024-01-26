def get_middle(s):
    import math
    list_s = list(s)
    length = len(list_s)
    for element in list_s:
        if length % 2 == 0:
            return list_s[int(length/2-1)] + list_s[int(length/2)]
        else:
            return list_s[math.floor(length/2)]
    
print(get_middle("test"))
print(get_middle("middle"))
print(get_middle('Tempvik'))