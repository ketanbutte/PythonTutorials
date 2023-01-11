from collections import OrderedDict

od = OrderedDict()

n = int(input())

for i in range(n):
    
    key, value = input().rsplit(maxsplit=1)
    od[key] = od.get(key) + int(value)
    
print(od)