'''
@Author: Sai Tarun
@Date: 2022-04-07 17: 05: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-07 14: 50: 00
@Title: Gambler.
'''
import random
def rand_num():
    """
        Description:
            Used to return random value.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns random integer value. 
    """
    value=random.randint(0,1)
    return value
def gambler_fun():
    """
        Description:
            takes user input for required fields and calculate the trail amount until no of trails.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints the win and loss percentages. 
    """
    stake_amount=int(input("Enter the stake amount: "))
    goal_amount=int(input("Enter the amount which you want to win: "))
    no_of_trails=int(input("Enter the number of trails: "))
    for i in range(no_of_trails):    
        win=0
        money=stake_amount
        noOfTimesWin=0
        while money > 0 and money < goal_amount:
            check=random.randint(0,1)      # check gambeler win or loss
            if check==win:
                money+=1
            else:
                money-=1

        if money==goal_amount:
            noOfTimesWin+=1
    winPercent=(noOfTimesWin/no_of_trails)*100
    print("Percentage of win ", winPercent)
    print("Percentage of loss ", 100-winPercent)
    
if __name__ == '__main__':
    gambler_fun()
