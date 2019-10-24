import time
from multiprocessing import Process, Queue
from progressBarInside import ProgressBarInside

class ProgressBar:

    def __init__(self, tam, length=50):
        self.q = Queue()
        self.qin = Queue()
        self.p = Process(target=ProgressBarInside, args=(tam, length, self.q, self.qin))
        self.p.start()

        self.counter = 1
        self.q.put(self.counter)

    def step(self):
        self.counter = self.counter + 1
        self.q.put(self.counter)

        while self.qin.empty():
            pass

        data = self.qin.get()
        print(data)
        print(data, end="\r")

if __name__ == '__main__':
    h = ProgressBar(49, 50)
    for i in range(1, 50):
        time.sleep(0.2)
        h.step()
