from threading import Timer
import logging

class PomodoroTimer:
    def __init__(self, workingMinutes, restMinutes):
        self.workingSeconds = workingMinutes * 60
        self.restSeconds = restMinutes * 60
        self.stopWorkEvent = []
        self.startWorkEvent = []
        self.startRestEvent = []
        self.stopRestEvent = []

    def _addListener(self, eventCollection, listener):
       if listener not in eventCollection:
           eventCollection.append(listener)

    def _removeListener(self, eventCollection, listener):
        if listener in eventCollection:
            eventCollection.remove(listener)

    def addStopWorkListener(self, listener):
        self._addListener(self.stopWorkEvent, listener)

    def removeStopWorkListener(self, listener):
        self._removeListener(self.stopWorkEvent, listener)

    def addStartWorkListener(self, listener):
        self._addListener(self.startWorkEvent, listener)

    def removeStartWorkListener(self, listener):
        self._removeListener(self.startWorkEvent, listener)

    def addStopRestListener(self, listener):
        self._addListener(self.stopRestEvent, listener)

    def removeStopRestListener(self, listener):
        self._removeListener(self.stopRestEvent, listener)

    def addStartRestListener(self, listener):
        self._addListener(self.startRestEvent, listener)


    def removeStartRestListener(self, listener):
        self._removeListener(self.startRestEvent, listener)


    def addAllListeners(self, listener):
        self.addStartWorkListener(listener)
        self.addStartRestListener(listener)
        self.addStopWorkListener(listener)
        self.addStopRestListener(listener)


    def removeAllListeners(self, listener):
        self.removeStartWorkListener(listener)
        self.removeStartRestListener(listener)
        self.removeStopWorkListener(listener)
        self.removeStopRestListener(listener)


    def startWork(self):
        self.notifyStartWork("Start of work time")
        self.timer = Timer(self.workingSeconds, self.stopWork)
        self.timer.start()

    def stopWork(self, startRestAfter = True):
        if hasattr(self, 'timer'):
            self.timer.cancel()
        self.notifyStopWork("End of work time", startRestAfter)
        if startRestAfter:
            self.startRest()


    def startRest(self):
        self.notifyStartRest("Start of rest time")
        self.timer = Timer(self.restSeconds, self.stopRest)
        self.timer.start()


    def stopRest(self, startWorkAfter = True):
        if hasattr(self, 'timer'):
            self.timer.cancel()
        self.notifyStopRest("End of rest time", startWorkAfter)
        if startWorkAfter:
            self.startWork()


    def notifyStartWork(self, message):
        for listener in self.startWorkEvent:
            listener.notifyStartWork(message)


    def notifyStopWork(self, message, startRestAfter):
        for listener in self.stopWorkEvent:
            listener.notifyStopWork(message, startRestAfter)


    def notifyStartRest(self, message):
        for listener in self.startRestEvent:
            listener.notifyStartRest(message)


    def notifyStopRest(self, message, startWorkAfter):
        for listener in self.stopRestEvent:
            listener.notifyStopRest(message, startWorkAfter)
