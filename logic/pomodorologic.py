import pdb
import asyncio
import threading
from pubsub import pub

class Pomodoro():
    '''This class handles the logic of a pomodoro timer.
    There are 6 events that the system will raise:
    * onStartOfWork
    * onEndOfWork
    * onStartOfRest
    * onEndOfRest
    * onCancelWork
    * onCancelRest

    If you want to do react to them you will need to subscribe'''
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



class PomodoroManager():
    '''This class will handle the run of one or more pomodoros'''
    
    def __init__(self, workTime, restTime):
        self.workTime = workTime
        self.restTime = restTime
        self.number_of_pomodoros = 0
        self.running = False
        
    def do_pomodoro(self):
            self.pomodoro = Pomodoro(self.workTime, self.restTime)
            self.pomodoro.startWork()

    def set_number_of_sessions(self, number_of_pomodoros):
        self.number_of_pomodoros = number_of_pomodoros

    @asyncio.coroutine
    def run_pomodoros(self):
        self.do_pomodoro()
        while self.number_of_pomodoros > 0:
            pass
    
    def execute_runner(self):
        self.running = True
        task = asyncio.Task(self.run_pomodoros())

        def finish_execution(task):
            loop = asyncio.get_event_loop()
            loop.stop()
            pub.unsubscribe(self.endOfRest, 'onEndOfRest')
            pub.unsubscribe(self.endOfWork, 'onEndOfWork')

        task.add_done_callback(finish_execution)
            
    def start(self):
        '''Starts a new pomodoro session in a thread
           The use of threads is for the run to be non-blocking. 
           Which will be important for any work done on GUI'''
        pub.subscribe(self.endOfRest, 'onEndOfRest')
        pub.subscribe(self.endOfWork, 'onEndOfWork')
        loop = asyncio.get_event_loop()
        self.execute_runner()
        loop.run_forever()

    def endOfRest(self):
        self.number_of_pomodoros -= 1
        self.do_pomodoro()

    def endOfWork(self):
        self.pomodoro.startRest()
