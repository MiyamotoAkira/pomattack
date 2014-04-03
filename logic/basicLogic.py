from threading import Timer


class PomodoroTimer:
    def __init__(self, workingMinutes, restMinutes):
        self.workingSeconds = workingMinutes * 60
        self.restSeconds = restMinutes * 60
        self.stopEvent = []

    def addListener(self, listener):
        if listener not in self.stopEvent:
            self.stopEvent.append(listener)

    def removeListener(self, listener):
        if listener in self.stopEvent:
            self.stopEvent.remove(listener)

    def startWork(self):
        timer = Timer(self.workingSeconds, self.endWork)
        timer.start()

    def endWork(self):
        self.notifyEnd("End of work time")
        timer = Timer(self.restSeconds, self.endRest)
        timer.start()

    def endRest(self):
        self.notifyEnd("End of rest time")

    def notifyEnd(self, message):
        for listener in self.stopEvent:
            listener.notifyEnd(message)
