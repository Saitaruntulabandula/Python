'''
@Author: Sai Tarun
@Date: 2022-04-05 20: 50: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-05 21: 40: 00
@Title: 2D Array.
'''
def fun_array():
    """
        Description:
            Takes the user input for rows and cols and elements to create 2d array.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints 2D Array. 
    """
    rows = int(input("Enter Number of Rows: "))
    cols = int(input("Enter number of columns: "))
    arr=[]
    for i in range(rows):
        arr.append([0]*cols)
    
    for i in range(rows):
        for j in range(cols):
            arr[i][j]=int(input("Enter the element value:"))
    
    for i in range(len(arr)):
        print(*arr[i],sep=" ")
if __name__ == '__main__':
    fun_array()
