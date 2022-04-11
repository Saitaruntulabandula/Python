'''
@Author: Sai Tarun
@Date: 2022-04-04 18: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-04 18: 35: 00
@Title: Harmonic Number
'''
def harmonicNum():
    """
        Description:
            Prints the  Harmonic Number
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints Harmonic Number. 
    """
    total=1
    n=int(input("Enter the value of n:"))
    for i in range(2,n+1):
        total=total+(1/i)
    print(total)
harmonicNum()