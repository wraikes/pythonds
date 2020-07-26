import random
import time


def del_set(n):
    d = {str(x): x for x in range(n)}
    l = [x for x in range(n)]
    ix = random.randint(0, n-1) 

    start_list = time.time()
    del l[ix]
    end_list = time.time()

    start_dict = time.time()
    del d[str(ix)]
    end_dict = time.time()

    print('List time: {}'.format(end_list-start_list))
    print('Dict time: {}'.format(end_dict-start_dict), end='\n\n')


if __name__=='__main__':
    count = 10

    for i in range(1, 4):
        print('Sample: {}'.format(100**i))
        del_set(100**i)

