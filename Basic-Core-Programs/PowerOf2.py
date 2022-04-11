'''
@Author: Sai Tarun
@Date: 2022-04-04 07: 29: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-04 07: 30: 00
@Title: Power of 2
'''
def power_of():
    """
        Description:
            Function is used to find power of 2 for the given number.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints power of 2 for the given number.
    """
    value=1
    N = int(input("Enter the Value of Exponent: "))
    if N<32:
        for i in range(N):
            if i<=N:
                value=value*2
        print("the value of 2 power N is : ",value)   #2*2*2*2*2*2
    else:
        print("N range should be below 32")
power_of()