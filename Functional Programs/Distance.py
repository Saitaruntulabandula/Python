'''
@Author: Sai Tarun
@Date: 2022-04-05 18: 50: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-05 18: 54: 00
@Title: Distance Between two points.
'''
import math
import sys
def fun_distance(x1,y1,x2,y2):
    """
        Description:
            Takes parameters and calculates euclidean distance and prints it.
        Parameter:
            Passed parameters x1,y1,x2,y2. 
        Return:
            Returns nothing but prints Euclidean distance. 
    """
    euclidean_distance=round(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)*1.0),2)
    print("Euclidean distance between given two points is",euclidean_distance)
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])
print("List of arguments are {} {} {} {}".format(a,b,c,d))
if __name__ == '__main__':
    fun_distance(a,b,c,d)



