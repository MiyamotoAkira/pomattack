from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock
from datetime import timedelta
from datetime import datetime

class MainWindow(Widget):
    informationToShow = StringProperty('')
    timeLeft = StringProperty('')

    def initialize(self, workTime, restTime):
        self.informationToShow = 'Something to show'
        self.workTime = workTime
        self.restTime = restTime
        self.notifyStartWork('test')


    def update(self, timeElapsed):
        elapsed = (datetime.now() - self.start)
        self.timeLeft = self.formatTime(self.calculateTimeLeft(elapsed).seconds)


    def formatTime(self, totalSeconds):
        minutes, seconds = divmod(totalSeconds, 60)
        return '%02d:%02d' % (minutes, seconds)

    def notifyStartWork(self, message):
        self.isWorkTime = True
        self.changeInformationMessage(message)
        self.startTimer()
        

    def notifyStopWork(self, message):
        self.changeInformationMessage(message)
        self.stopTimer()


    def notifyStartRest(self, message):
        self.isWorkTime = False
        self.changeInformationMessage(message)
        self.startTimer()


    def notifyStopRest(self, message):
        self.changeInformationMessage(message)
        self.stopTimer()


    def changeInformationMessage(self, message):
        self.informationToShow = message


    def startTimer(self):
        Clock.schedule_interval(self.update, 1.0)
        self.start = datetime.now()


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
        Clock.unschedule(self.update)


class PomodoroUIApp(App):
    def build(self):
        window = MainWindow()
        window.initialize(25, 5)
        return window


if __name__ == '__main__':
    PomodoroUIApp().run()
