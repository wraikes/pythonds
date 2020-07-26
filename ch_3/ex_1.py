import random
import time

def index(n):
    l = list(range(n))
    ix = random.randint(0, n-1) 

    start = time.time()
    val = l[ix]   
    end = time.time()

    print('Time: {}'.format(end-start), end='\n\n')


if __name__=='__main__':
    count = 10

    for i in range(1, 5):
        print(''.format(100**i))
        index(10**i)

