def divisible_by(numbers, divisor):
    divisible = []
    for num in numbers:
        if num % divisor == 0:
            divisible.append(num)
    return(divisible)
print(divisible_by([1,2,3,4,5,6,7,8],2))
print(divisible_by([1,2,3,4,5,6],3))
