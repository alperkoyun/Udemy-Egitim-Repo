"""
def double(x):
    return x * 2
a= list(map(double,[1,2,3,4,5,6,7]))
print(a)

a2 =list(map(lambda x : x ** 2,(1,2,3,4,5,6,7,8,9,10)))
"""
liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]
a4 = list(map(lambda x,y,z : x * y * z, liste1,liste2,liste3))
print(a4)