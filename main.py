# the goal is to time how much time spent on a project and add it all up
# so I need it to keep track in seconds, then convert to hours or minutes
# I also need it to keep track of multiple sessions

import time, sys

def timer():
    totalTime = 0
    try:
        while True:
            time.sleep(1)
            totalTime += 1
            print(totalTime, end='\r', flush=True)
    except KeyboardInterrupt:
        print('total time was : ', convert(totalTime))
        with open('totalTimeFile.txt', 'a') as f:
            f.write(str(totalTime) + '\n')

def addTime():
    absoluteTime = 0
    with open('totalTimeFile.txt', 'r') as f:
        for line in f:
            absoluteTime += int(line)
        with open('totalTimeFile.txt', 'w') as s:
            s.write('')
        print(convert(absoluteTime))


def currentTime():
    absoluteTime = 0
    with open('totalTimeFile.txt', 'r') as f:
        for line in f:
            absoluteTime += int(line)
        print(convert(absoluteTime))

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 




def choice(x):
    if(x == 'n'):
        timer()
    if(x == 'd'): 
        addTime()
    if(x == 'c'):
        currentTime()

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print('Not enough arguments')
        print('n for new, d for done with current project: ')
    else:
        try:
            choice(sys.argv[1])
        except:
            raise TypeError