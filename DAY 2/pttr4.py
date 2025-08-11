#      *
#     ***
#    *****
#   *******
#  *********
# *********** 
#  *********
#   *******
#    *****
#     ***
#      *

# Tracing Table
# -------------------    n , m = (n + 1) // 2
# i     *       _ 
# -------------------
# 1     1       5      stars = 2 * i - 1
# 2     3       4      spaces = m - i 
# 3     5       3
# 4     7       2
# 5     9       1
# 6     11      0
# ==================== m 
# 7     9       1     stars = 2 * ((n + 1) - i) - 1
# 8     7       2     spaces = i - m
# 9     5       3
# 10    3       4 
# 11    1       5
# -------------------

# n = int(input("Please Enter the number of Rows (ODD): "))

# m = (n + 1) // 2
# for i in range(1, n + 1):
#     if i <= m:
#         stars = 2 * i - 1
#         spaces = m - i
#         print(" " * spaces + "*" * stars)
#     else:
#         stars = 2 * ((n + 1) - i) - 1
#         spaces = i - m
#         print(" " * spaces + "*" * stars)
        
        
# Tracing Table
# -------------------    n , m = (n + 1) // 2
# i     *       _ 
# -------------------
# 1     1       5      stars = 2 * i - 1
# 2     3       4      spaces = m - i 
# 3     5       3
# 4     7       2
# 5     9       1
# ====================
# 6     11      0
# ==================== m 
# 7     9       1     stars = 2 * ((n + 1) - i) - 1
# 8     7       2     spaces = i - m
# 9     5       3
# 10    3       4 
# 11    1       5
# -------------------

n = int(input("Please Enter the number of Rows (ODD): "))

m = (n + 1) // 2
for i in range(1, n + 1):
    if i < m:
        stars = 2 * i - 1
        spaces = m - i
        print(" " * spaces + "*" * stars)
    elif i == m:
        print("*" * n)
    else:
        stars = 2 * ((n + 1) - i) - 1
        spaces = i - m
        print(" " * spaces + "*" * stars)