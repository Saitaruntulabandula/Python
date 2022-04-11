'''
@Author: Sai Tarun
@Date: 2022-04-05 19: 40: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-05 19: 57: 00
@Title: Find the roots of the equation.
'''
import cmath
def user_input():
    """
        Description:
            Takes the user input for a,b,c.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns x,y,z values. 
    """
    x=int(input("Enter the value of a: "))
    y=int(input("Enter the value of b: "))
    z=int(input("Enter the value of c: "))
    return x,y,z
def find_roots():
    """
        Description:
            Takes the user input for a,b,c from user_input function.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints the roots of given quadratic equation. 
    """
    a,b,c=user_input()
    root1=(-b+cmath.sqrt((b*b)-(4*a*c)))/(2*a)
    root2=(-b-cmath.sqrt((b*b)-(4*a*c)))/(2*a)
    print("The roots of the given quadratic equation is",root1,root2)
if __name__ == '__main__':
    find_roots()