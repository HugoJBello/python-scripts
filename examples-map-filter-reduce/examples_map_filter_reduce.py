
from functools import reduce

array = [1,2,3,4,5,6,7,8,9,10]
print ("numbers ",array)
#map(function_to_apply, list_of_inputs)

squared_array = list(map(lambda x:x*x, array ))
print ("squared numbers in array ", squared_array)

lesser_than_4 = list(filter(lambda x: x<4, array ))
print ("numbers lesser than 4 ", lesser_than_4)


max = reduce((lambda x,y: x if (y<x) else y),array)
print("max ", max)

min = reduce((lambda x,y: x if (y>x) else y),array)
print("min", min)