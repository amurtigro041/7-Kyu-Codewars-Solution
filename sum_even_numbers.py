def sum_even_numbers(seq): 
    even_numbers = []
    if seq == None:
        return 0
    else:
        for x in seq:
            if x % 2 == 0:
                even_numbers.append(x)
    solve = sum(even_numbers)
    return solve
print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))