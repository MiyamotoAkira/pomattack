import unittest
import sys
from mock import Mock
from pomattack.ui.mainWindow import MainWindow
from datetime import timedelta

class MainWindowTestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'message'


    def createWindow(self):
        window = MainWindow()
        mockPomodoro = Mock()
        window.initialize(25,5, mockPomodoro)
        return window


    def test_notifyStartWorkIsCalled_InformationToShowIsChanged(self):
        window = self.createWindow()
        window.notifyStartWork(self.message)
        self.assertEqual(window.informationToShow, self.message)


    def test_notifyEndWorkIsCalled_InformationToShowIsChanged(self):
        window = self.createWindow()
        window.notifyStopWork(self.message)
        self.assertEqual(window.informationToShow, self.message)


    def test_notifyStartRestIsCalled_InformationToShowIsChanged(self):
        window = self.createWindow()
        window.notifyStartRest(self.message)
        self.assertEqual(window.informationToShow, self.message)


    def test_notifyEndRestIsCalled_InformationToShowIsChanged(self):
        window = self.createWindow()
        window.notifyStopRest(self.message)
        self.assertEqual(window.informationToShow, self.message)


    def test_calculateTimeLeft_25MinTotalnoElapsedTime_25MinTimeLeft(self):
        window = self.createWindow()
        window.isWorkTime = True
        elapsedTime = timedelta(seconds=0)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=25))


    def test_calculateTimeLeft_25MinTotalOneMinuteElapsedTime_24MinTimeLeft(self):
        window = self.createWindow()
        window.isWorkTime = True
        elapsedTime = timedelta(minutes=1)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=24))


    def test_calculateTimeLeft_25MinTotal25MinElapsed_0MinTimeLeft(self):
        window = self.createWindow()
        window.isWorkTime = True
        elapsedTime = timedelta(minutes=25)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=0))


    def test_calculateTimeLeft_25MinTotal25Min1SecElapsed_0MinTimeLeft(self):
        window = self.createWindow()
        window.isWorkTime = True
        elapsedTime = timedelta(minutes=25, seconds = 1)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=0))


    def test_getTimeUsed_isWorkTime_returns25(self):
        window = self.createWindow()
        window.isWorkTime = True
        timeUsed = window.getTimeUsed()
        self.assertEqual(timeUsed, 25)


    def test_getTimeUsed_isNotWorkTime_returns5(self):
        window = self.createWindow()
        window.isWorkTime = False
        timeUsed = window.getTimeUsed()
        self.assertEqual(timeUsed, 5)


    def test_callStartTimerTwice_doesNotFail(self):
        window = self.createWindow()
        window.isWorkTime = True
        window.startTimer()
        window.startTimer()

