#      *
#     **
#    ****
#   ******
#  ******** 

# Tracing Table
# -------------------
# i     *       _  
# -------------------
# 1     1       4
# 2     2       3
# 3     4       2
# 4     6       1
# 5     8       0
# -------------------

n = int(input("Please Enter the number of Rows: "))

for i in range(1, n + 1):
    if i == 1:
        stars = 1
    else:
        stars = 2 * i - 2
    spaces = n - i
    print(" " * spaces + "*" * stars)
    