import threading
import time

class MyThread(threading.Thread):
    def __init__(self, thread_no):
        super().__init__()
        self.thread_no = thread_no

    def run(self):
        for count in range(10):
            print("Thread {} count {}".format(self.thread_no, count))
            time.sleep(0.25)


if __name__ == '__main__':
    for x in range(4):
        my_thread = MyThread(x)
        my_thread.start()
