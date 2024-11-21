import hashlib
import time
from multiprocessing import Process, cpu_count
string = "por que?"
zeros = 8

def logan(nonce):
    start_time = time.time()
    nonce1 = nonce
    bhash = '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
    zerostr = '0'*zeros
    cpu_counts = cpu_count()
    while bhash[:zeros]!=zerostr:
        bhash = hashlib.sha256(bytes(string+str(nonce1), 'utf-8')).hexdigest()
        nonce1 += cpu_counts
    nonce1 -= cpu_counts
    end_time = time.time()
    print("Done!")
    print(bhash)
    print(string+str(nonce1))
    print(end_time-start_time)
    
 


if __name__ == '__main__':
    thread_count = cpu_count()
    threads = [Process(target=logan, args=(y,)) for y in range(thread_count)]
    # t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16 = Process(target=logan, args=(0,)), Process(target=logan, args=(1,)),Process(target=logan, args=(2,)),Process(target=logan, args=(3,)),Process(target=logan, args=(4,)),Process(target=logan, args=(5,)),Process(target=logan, args=(6,)),Process(target=logan, args=(7,)),Process(target=logan, args=(8,)),Process(target=logan, args=(9,)),Process(target=logan, args=(10,)),Process(target=logan, args=(11,)),Process(target=logan, args=(12,)),Process(target=logan, args=(13,)),Process(target=logan, args=(14,)),Process(target=logan, args=(15,)),
    # threads = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16]
    for i in threads:
        i.start()
    while not any([x.is_alive() == False for x in threads]):
        pass
    for i in threads:
        i.terminate()