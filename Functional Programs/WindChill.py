'''
@Author: Sai Tarun
@Date: 2022-04-05 19: 40: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-05 19: 57: 00
@Title: Find the wind chill by using speed and temperature.
'''

import math
import sys

def speed(a):
    if a>120 or a<3:
        print("Enter valid speed")
        speed()
    else:
        x=a
        print("You have entered valid speed: ",a)
    return x
def temperature(b):

    if b>50:
        print("Enter valid temperature")
        temperature()
    else:
        y=b
        print("You have entered valid temperature: ",b)
    return y
def wind_chill():
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    wind_speed=speed(a)
    var_temp=temperature(b)
    wind_chill_condition=35.74+0.6215*var_temp+(0.4275*var_temp+35.74)*(math.pow(wind_speed,0.16))
    print("Condition of the wind chill is :",wind_chill_condition)
if __name__ == '__main__':
    wind_chill()