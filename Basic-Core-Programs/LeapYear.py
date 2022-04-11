'''
@Author: Sai Tarun
@Date: 2022-04-04 07: 17: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-04 07: 18: 00
@Title: Leap year or not.
'''
def leap_year():
    """
        Description:
            Function is used to find weather the given year is leap or not.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints that given year is leap or not.
    """
    year=int(input('Enter the year:'))
    if year>999 and year<10000:
        if ((year%4==0 and year%100!=0) or (year%400==0)):
            print('Leap Year')
        else:
            print('Not a Leap year')
    else:
        print("Enter a valid 4 digit year")
        leap_year()
leap_year()