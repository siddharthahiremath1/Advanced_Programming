import hashlib
import time
from multiprocessing import Process
import random
string = "freedom"
zeros = 7
nhash = '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

def logan(nonce):
    nonce1 = nonce
    bhash = '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
    zerostr = '0'*zeros 
    while bhash[:zeros]!=zerostr:
        bhash = hashlib.sha256(bytes(string+str(nonce1), 'utf-8')).hexdigest()
        nonce1 += 16
    end_time = time.time()
    
    print("Done!")
    print(bhash)
    print(string+str(nonce1))
    print(end_time-start_time)
start_time = time.time()

if __name__ == "__main__":
    t1 = Process(target=logan, args=(0,))
    t2 = Process(target=logan, args=(1,))
    t3 = Process(target=logan, args=(2,))
    t4 = Process(target=logan, args=(3,))
    t5 = Process(target=logan, args=(4,))
    t6 = Process(target=logan, args=(5,))
    t7 = Process(target=logan, args=(6,))
    t8 = Process(target=logan, args=(7,))
    t9 = Process(target=logan, args=(8,))
    t10 = Process(target=logan, args=(9,))
    t11 = Process(target=logan, args=(10,))
    t12 = Process(target=logan, args=(11,))
    t13 = Process(target=logan, args=(12,))
    t14 = Process(target=logan, args=(13,))
    t15 = Process(target=logan, args=(14,))
    t16 = Process(target=logan, args=(15,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()

