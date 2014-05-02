from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from datetime import timedelta
from datetime import datetime
from pomattack.logic.basicLogic import PomodoroTimer
import logging

class MainWindow(BoxLayout):
    informationToShow = StringProperty('')
    timeLeft = StringProperty('')
    currentFormat = StringProperty('')

    def initialize(self, workTime, restTime, pomodoro):
        logging.basicConfig(level=logging.DEBUG)
        self.informationToShow = 'Something to show'
        self.workTime = workTime
        self.restTime = restTime
        self.currentFormat = 'On Work'
        self.isWorkTime = True
        self.isRunning = False
        self.pomodoro = pomodoro
        self.pomodoro.addAllListeners(self)


    def update(self, timeElapsed):
        elapsed = (datetime.now() - self.startingTime)
        self.timeLeft = self.formatTime(self.calculateTimeLeft(elapsed).seconds)


    def formatTime(self, totalSeconds):
        minutes, seconds = divmod(totalSeconds, 60)
        return '%02d:%02d' % (minutes, seconds)


    def changeFormat(self):
        self.isWorkTime = not self.isWorkTime
        if self.isWorkTime:
            self.currentFormat = 'On Work'
        else:
            self.currentFormat = 'On Rest'


    def onStartStop(self):
        if not self.isRunning:
            self.start()
        else:
            self.stop()


    def start(self):
        if self.isWorkTime:
            self.pomodoro.startWork()
        else:
            self.pomodoro.startRest()


    def stop(self):
        if self.isWorkTime:
            self.pomodoro.stopWork(False)
        else:
            self.pomodoro.stopRest(False)


    def notifyStartWork(self, message):
        self.startTimer()
        self.changeInformationMessage(message)
        

    def notifyStopWork(self, message, startRestAfter):
        self.changeInformationMessage(message)
        self.stopTimer()
        if startRestAfter:
            self.changeFormat()
            self.startTimer()


    def notifyStartRest(self, message):
        self.startTimer()
        self.changeInformationMessage(message)


    def notifyStopRest(self, message, startWorkAfter):
        self.changeInformationMessage(message)
        self.stopTimer()
        if startWorkAfter:
            self.changeFormat()
            self.startTimer()


    def changeInformationMessage(self, message):
        self.informationToShow = message


    def startTimer(self):
        self.isRunning = True
        Clock.schedule_interval(self.update, 1.0)
        self.startingTime = datetime.now()

        
    def getTimeUsed(self):
        if self.isWorkTime:
            return self.workTime
        else:
            return self.restTime


    def calculateTimeLeft(self, elapsed):
        timeUsed = self.getTimeUsed()
        timeLeft = timedelta(minutes=timeUsed)-elapsed
        if timeLeft.total_seconds() > 0:
            return timeLeft
        else:
            return timedelta(seconds=0)
    

    def stopTimer(self):
        self.isRunning = False
        Clock.unschedule(self.update)


class PomodoroUIApp(App):
    def build(self):
        self.window = MainWindow()
        minutesWork = 2
        minutesRest = 1
        pomodoro = PomodoroTimer(minutesWork, minutesRest)
        self.window.initialize(minutesWork, minutesRest, pomodoro)
        return self.window

    
    def on_stop(self):
        self.window.stop()
        Clock.unschedule(self.window.update)


if __name__ == '__main__':
    PomodoroUIApp().run()
