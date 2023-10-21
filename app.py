import os
import time
import SecondsClock
if __name__ == "__main__":
    while True:
        print("-----------------------")
        print("S*E*C*O*N*D* W+A+T+C+H\n")
        print("SE\tSeconds Elapsed")
        print("SR\tSeconds Remaining")
        print("-----------------------")
        SC = SecondsClock.SecondsClock()
        SC.update()
        time.sleep(1)
        os.system("clear")
        if SC.total_time_in_seconds >= SC.total_seconds_in_day:
            SC.reset()
