import random

times = int(input("Times: "))
dic = dict()

def iterations(var):
    for x in range(var):
        rand = random.randint(1,6) + random.randint(1,6)
        dic[rand] = dic.get(rand, 0) + 1
    
iterations(times)
print(dic)