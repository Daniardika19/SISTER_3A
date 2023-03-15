#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def myFunc(i):
    print ('memanggil proses ke: %s' %i)
    for j in range (0,i):
        print('hasil dari proses myFunc :%s' %j)
    return

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
