import random
import time

def dict_set(n):
    d = {str(x): x for x in range(n)}
    ix = random.randint(0, n-1) 

    start = time.time()

    d[n+1] = n+1
    d[str(ix)]

    end = time.time()

    print('Time: {}'.format(end-start), end='\n\n')


if __name__=='__main__':
    count = 10

    for i in range(1, 4):
        print('Sample: {}'.format(100**i))
        dict_set(100**i)

