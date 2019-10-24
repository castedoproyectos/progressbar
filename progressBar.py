from os import system, name

# import sleep to show output for some time period
import time
class ProgressBar:

    def __init__(self, numSteps, length):
        self.__numStep = numSteps
        self.__length = length
        self.__stepValue = length/numSteps
        self.__actualValuePerc = 0
        self.__actualValue = 1
        self.__progressTime = time.perf_counter()

    def step(self):
        self.__actualValue = self.__actualValue + 1
        self.__actualValuePerc = self.__actualValue*self.__stepValue
        self.print()

    def print(self):
        iactualValuePerc = int(round(self.__actualValuePerc, 0))
        if iactualValuePerc == 0:
            iactualValuePerc = 1
        bar = '=' * (iactualValuePerc - 1) + ">" + ' ' * (self.__length - iactualValuePerc)
        print("|" + bar + "| " + str(self.__actualValue) + "/" + str(self.__numStep) + "(" + str(round(self.__actualValuePerc, 1)) + ")" + str(self.__progressTime))


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__ == '__main__':
    progressBar = ProgressBar(100,45)
    progressBar.print()
    for a in range(1,100):
        time.sleep(1)
        clear()
        progressBar.step()






