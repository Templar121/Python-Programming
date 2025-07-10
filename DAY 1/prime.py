def is_prime(n):
    if n == 1:
        print("Neither Prime nor Composite")
        return
    if n == 2:
        print("Is Prime")
        return
    if n % 2 == 0:
        print("Is Not Prime or Is Composite")
        return
        
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            print("Is Not Prime or Is Composite")
            return 
    print("Is Prime")
    
is_prime(25)