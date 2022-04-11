'''
@Author: Sai Tarun
@Date: 2022-04-07 12: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-07 14: 50: 00
@Title: Coupon Numbers.
'''
import random
def coupon_numbers(n):
    """
        Description:
            Takes the parameter n for count of random distinct numbers.
        Parameter:
            Passed parameter n. 
        Return:
            Returns nothing but prints the coupon number with distinct digits in it. 
    """
    list=[]
    while len(list)<n:
        value=random.randint(0,n)
        if value not in list:
            list.append(value)
    print(*list,sep=" ")
if __name__ == '__main__':
    n=int(input("Enter the random numbers count: "))
    coupon_numbers(n)