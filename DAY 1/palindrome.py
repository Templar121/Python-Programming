def palindrome(a):
    if str(a) == str(a)[::-1]:
        print("Is Palindrome")
    else:
        print("Is Not Palindrome")
        
palindrome(12345)