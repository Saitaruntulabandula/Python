'''
@Author: Sai Tarun
@Date: 2022-04-03 15: 00: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-03 15: 06: 00
@Title: Head and Tail Percentage
'''

import random
n = int(input("enter the Number:"))
def percentage():
    """
        Description:
            Function is used to get the percentage of heads and tails.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints the percentage of heads and tails.
    """
    count_of_heads = 0
    count_of_tails = 0
    for i in range(n):
        result=random.randint(0, 1)
        if result == 0:
            count_of_heads+=1

    count_of_tails=n-count_of_heads
    print("Heads count", count_of_heads)
    print("Tails count", count_of_tails)

    percentage_head = ((count_of_heads*100)/n)
    print("Head percentage:", percentage_head)

    print("Tail percentage:",(100-percentage_head))
percentage()