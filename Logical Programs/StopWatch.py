'''
@Author: Sai Tarun
@Date: 2022-04-07 15: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-07 16: 20: 00
@Title: Stop Watch.
'''
import time

def stop_watch():
    """
        Description:
            takes response with enter button and as a result prints lapsed time.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints the lapsed time between enter button reponses. 
    """
    input("Press Enter to start: ")
    start_time = time.time()

    input("Press Enter to stop: ")
    end_time = time.time()

    time_lapsed = end_time - start_time
    print("Lapsed time between start and stop is",time_lapsed,"Seconds")
if __name__ == '__main__':
    stop_watch()