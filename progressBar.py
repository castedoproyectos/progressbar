import time
from multiprocessing import Process, Queue
from os import system, name

from progressBarInside import ProgressBarInside


def clearConsole():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


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

        clearConsole()
        data = self.qin.get()
        print(data)


if __name__ == '__main__':
    h = ProgressBar(49, 50)
    for i in range(1,50):
        time.sleep(0.1)
        h.step()
