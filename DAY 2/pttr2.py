# *********
#  *******
#   *****
#    ***
#     *

# Tracing table
# ----------------
# i    *   _
# ----------------
# 1    9   0
# 2    7   1
# 3    5   2 
# 4    3   3
# 5    1   4
# ---------------- 

n = int(input("Please Enter the number of Rows: "))
for i in range(1, n + 1):
    stars =  ((n - i) * 2) + 1
    spaces = i - 1
    print(" " * spaces + "*" * stars)