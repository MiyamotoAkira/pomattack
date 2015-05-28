import threading
from pubsub import pub

class Pomodoro():
    '''This class handles the logic of a pomodoro timer'''
    def __init__(self, workTime=0, restTime=0):
        '''workTime and restTime are the values used for the timer.
        They are indicated in seconds'''
        self.workTime = workTime
        self.restTime = restTime

    def startWork(self):
        self.OnStartOfWork()
        self.workTimer = threading.Timer(self.workTime, self.OnEndOfWork)
        self.workTimer.start()

    def startRest(self):
        self.OnStartOfRest()
        self.restTimer = threading.Timer(self.restTime, self.OnEndOfRest)
        self.restTimer.start()

    def cancelWork(self):
        '''Tries to cancel the work timer. If it wasn't started, it will not fail, and will still raise the events. This behaviour is not guaranteed to remain as it is now. '''
        self.OnCancelWork()
        try:
            self.workTimer.cancel()
        except:
            pass
        self.OnEndOfWork()

    def cancelRest(self):
        '''Tries to cancel the rest timer. If it wasn't started, it will not fail, and will still raise the events. This behaviour is not guaranteed to remain as it is now. '''
        self.OnCancelRest()
        try:
            self.restTimer.cancel()
        except:
            pass
        self.OnEndOfRest()

    def OnStartOfWork(self):
        pub.sendMessage('onStartOfWork')

    def OnEndOfWork(self):
        pub.sendMessage('onEndOfWork')

    def OnStartOfRest(self):
        pub.sendMessage('onStartOfRest')

    def OnEndOfRest(self):
        pub.sendMessage('onEndOfRest')

    def OnCancelWork(self):
        pub.sendMessage('onCancelWork')

    def OnCancelRest(self):
        pub.sendMessage('onCancelRest')
