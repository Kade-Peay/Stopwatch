# the goal is to time how much time spent on a project and add it all up
# so I need it to keep track in seconds, then convert to hours or minutes
# I also need it to keep track of multiple sessions

import time, sys

def menu(x):
    if(x == 'n'):
        totalTime = 0
        try:
            while True:
                time.sleep(1)
                totalTime += 1
                print(totalTime, end='\r', flush=True)
        except KeyboardInterrupt:
            print('total time was : ', totalTime)
            with open('totalTimeFile.txt', 'a') as f:
                f.write(str(totalTime) + '\n')
    if(x == 'd'): 
        absoluteTime = 0
        with open('totalTimeFile.txt', 'r') as f:
            for line in f:
                absoluteTime += int(line)
        with open('totalTimeFile.txt', 'w') as s:
            s.write('')
        print(absoluteTime)
    
        

if __name__ == "__main__":
    print('n for new, d for done with current project: ')
    choice = input("choose: ")
    menu(choice)

# __main__()