#!/usr/bin/python
import threading
import time


exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程" + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s : %s " % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = myThread(1, "thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print("退出主线程")
