'''
@Author: Sai Tarun
@Date: 2022-04-04 19: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-04 19: 35: 00
@Title: Harmonic Number
'''

def factors():
    """
        Description:
            Function is used to find factors of the given number.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints the factors of the given number.
    """
    n=int(input("Enter the n value:"))
    for i in range(2,n):
        while n%i==0:
            print(i," ")
            n=n/i
factors()