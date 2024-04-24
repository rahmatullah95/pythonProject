#1+2+3+..........+n

"""
num = int(input("Enter the last number of the series: "))

sum = 0

for x in range(1,num+1,1):
    sum = sum + x
print(sum)
"""

# 2+4+6+....+n
"""
num = int(input("Enter the last number of the series: "))
sum = 0

for x in range(2,num+1,2):
    sum = sum + x
print(sum)
"""

# 1+3+5+ ..... + n
"""
num = int(input("Enter the last number of the series: "))
sum = 0

for x in range(1,num+1,2):
    sum = sum + x
print(sum)
"""

# 1*1 + 2*2 + 3*3 + ... + n*n

"""
num = int(input("Enter the last number of the series: "))
sum = 0

for x in range(1,num+1,1):
    sum = sum + x*x
print(sum)
"""

# 1x2x3x....xn
num = int(input("Enter the last number of the series: "))
sum = 1

for x in range(1,num+1,1):
    sum = sum * x*x
print(sum)