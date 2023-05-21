import math
p = 17
n = 69
sup = math.floor(math.log(n)/math.log(p))
li = []
for i in range(1,sup+1):
    result = math.floor(n/(p**i))
    li.append(result)
    
print(sum(li))
