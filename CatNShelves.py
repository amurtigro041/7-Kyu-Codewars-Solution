
def shelves_count(max_shelve,start_point):
#global variable
    global jump_range
    global n_jump
#describing the variable
    n_jump = 0
    while start_point < max_shelve:
        jump_range = max_shelve - start_point
        if jump_range >= 3:
            start_point += 3
            n_jump += 1
        elif jump_range < 3 :
            start_point += 1
            n_jump += 1
    return n_jump
            

print(shelves_count(6,1))
print(shelves_count(5,1))
print(6//3 + 6 % 3)