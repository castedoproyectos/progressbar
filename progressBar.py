from os import system, name

# import sleep to show output for some time period
import time
import timeit
class ProgressBar:

    def __init__(self, numSteps, length):
        self.__numStep = numSteps
        self.__length = length
        self.__stepValue = length/numSteps
        self.__actualValuePerc = 0
        self.__actualValue = 1
        self.__iniTime = timeit.default_timer()
        self.__progressTime = 0.0

    def _formatSeconds(self, seconds):

        mins = int(seconds / 60)
        secondsRest = round(seconds % 60)

        smins = str(mins)
        if len(smins) == 1:
            smins = "0" + smins

        sSecondRest = str(secondsRest)
        if len(sSecondRest) == 1:
            sSecondRest = "0" + sSecondRest

        return smins + ":" + sSecondRest

    def step(self):
        self.__actualValue = self.__actualValue + 1
        self.__actualValuePerc = round(100 * self.__actualValue / self.__numStep, 1)
        self.__progressTime = timeit.default_timer() - self.__iniTime
        self.print()

    def print(self):
        iactualValuePerc = int(round(self.__length * self.__actualValuePerc / 100))
        if iactualValuePerc == 0:
            iactualValuePerc = 1

        timeleft = round((self.__progressTime / self.__actualValue) * (self.__numStep - self.__actualValue))
        bar = '=' * (iactualValuePerc - 1) + ">" + ' ' * (self.__length - iactualValuePerc)
        print("|" + bar + "| "
              + str(self.__actualValue) + "/" + str(self.__numStep)
              + "\t(" + str(self.__actualValuePerc) + " %) "
              + "\t[" + self._formatSeconds(self.__progressTime) + " - " + self._formatSeconds(timeleft) + "]")


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__ == '__main__':
    progressBar = ProgressBar(10000,100)
    progressBar.print()
    for a in range(9999):
        time.sleep(1)
        #clear()
        progressBar.step()







