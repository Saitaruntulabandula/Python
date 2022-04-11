'''
@Author: Sai Tarun
@Date: 2022-04-05 18: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-05 18: 35: 00
@Title: Sum of Three numbers.
'''
def user_input():
    """
        Description:
            Takes range of list and append values to list.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns list. 
    """
    list=[]
    n=int(input("Enter the range:"))
    for i in range(n):
        value=int(input("Enter the value:"))
        list.append(value)
    return list
def sum_of_three():
    """
        Description:
            Prints list of combinations and number of combinations.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but list of combinations and number of combinations. 
    """
    count=0
    n=user_input()
    for i in range(len(n)):                      #loop for 1st element index
        for j in range(i + 1, len(n)):           #loop for 2st element index
            for k in range(j + 1, len(n)):       #loop for 3st element index
                if (n[i]+n[j]+n[k]) == 0:        #Adding three elemets to check result 
                    count=count+1
                    print("Combination",count,"is",n[i],n[j],n[k])
    print("Number of combinations are",count)
#n=[0, 1, -1, 2, -2, 3, -3, 4 ]
    
if __name__ == '__main__':
    sum_of_three()