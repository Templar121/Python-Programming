# Traditional Approach
def reverse(n):
    reverse_no = 0
    negative = n < 0
    n = abs(n)
    
    while n != 0:
        digit = n % 10
        reverse_no = (reverse_no * 10) + digit
        n //= 10
        
    print("-" + str(reverse_no)) if negative else print(reverse_no)
    
reverse(-14458)


# # String Reversal
# def reverse(n):
#     if n > 0:
#         print(str(n)[::-1])
#     else:
#         print("-" + str(n)[:0:-1])
    
# reverse(-14458)