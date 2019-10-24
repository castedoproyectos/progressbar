import timeit

class ProgressBarInside:

    def __init__(self, numSteps, length, memory, memoryout):
        self.__numSteps = numSteps
        self.__length = length
        self.__stepValue = length/numSteps
        self.__actualValuePerc = 0
        self.__actualValue = 1
        self.__iniTime = timeit.default_timer()
        self.__progressTime = 0.0
        self.__memory = memory
        self.__memoryout = memoryout

        self._running()

    def _running(self):
        while self.__actualValue < self.__numSteps:
            while not self.__memory.empty():
                self.__actualValue = self.__memory.get()
                self.step()

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
        self.__actualValuePerc = round(100 * self.__actualValue / self.__numSteps, 1)
        self.__progressTime = timeit.default_timer() - self.__iniTime
        self.print()

    def print(self):
        iactualValuePerc = int(round(self.__length * self.__actualValuePerc / 100))
        if iactualValuePerc == 0:
            iactualValuePerc = 1

        timeleft = round((self.__progressTime / self.__actualValue) * (self.__numSteps - self.__actualValue))
        bar = '=' * (iactualValuePerc - 1) + ">" + ' ' * (self.__length - iactualValuePerc)

        self.__memoryout.put("|" + bar + "| "
              + str(self.__actualValue) + "/" + str(self.__numSteps)
              + "\t(" + str(self.__actualValuePerc) + " %) "
              + "\t[" + self._formatSeconds(self.__progressTime) + " - " + self._formatSeconds(timeleft) + "]")









