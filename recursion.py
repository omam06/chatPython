def countdown(n):
    if n < 0:  #base case tell program when to stop, else it keeps going
        return
    print(n)
    countdown(n - 1)   #recursive case where func calls itself w a smaller problem (n-1)
    print('Done', n)
countdown(4)             #create another call to same func but w diff value

def countdown(n):
    if n == 0:
        return
    print('Down', n)
    countdown(n - 1)
    print('Up', n)
countdown(3)