import threading
import time
import os

counter = 0

def watcher():
    global counter
    for i in range(3):
        print("value of counter ",counter)
        time.sleep(1)

def update(lock):
    global counter
    with lock:
        for i in range(5):
            counter += 1
            time.sleep(1)

# def activity(tag):
#     for i in range(5):
#         print("Hello ",tag," i = ",i," thread_id = ",thread_id)
#         time.sleep(1)
#
# def worker1():
#     print("worker1 thread_id is ", threading.current_thread().ident)
#     activity("worker1")
#
# def worker2():
#     print("worker2 thread_id is ", threading.current_thread().ident)
#     activity("worker2")

def main():
    lock = threading.RLock()
    #print("main thread_id is ",threading.current_thread().ident)
    thread1 = threading.Thread(target=update,args=(lock,))
    thread2 = threading.Thread(target=update,args=(lock,))
    thread3 = threading.Thread(target=watcher)
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    print("final counter value",counter)

if __name__== "__main__":
    main()