from functools import reduce

liste1 = [1,2,3,4,5,6,7,8,9,10]

def toplama(x,y):
    return x+y

print(reduce(toplama,list(filter(lambda x: x % 2 == 0,liste1))))