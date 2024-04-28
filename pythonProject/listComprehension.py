num = [1,2,3,4,5]

#list conprehension for map
result = [x*x for x in num]
print(result)

#list conprehension for filter
result = [x for x in num if x%2==0]
print(result)