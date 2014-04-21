import unittest
import sys
from mock import Mock
from pomattack.ui.mainWindow import MainWindow
from datetime import timedelta

class MainWindowTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_notifyStartWorkIsCalled_InformationToShowIsChanged(self):
        message = 'message'
        window = MainWindow()
        window.notifyStartWork(message)
        self.assertEqual(window.informationToShow, message)


    def test_notifyEndWorkIsCalled_InformationToShowIsChanged(self):
        message = 'message'
        window = MainWindow()
        window.notifyStopWork(message)
        self.assertEqual(window.informationToShow, message)


    def test_notifyStartRestIsCalled_InformationToShowIsChanged(self):
        message = 'message'
        window = MainWindow()
        window.notifyStartRest(message)
        self.assertEqual(window.informationToShow, message)


    def test_notifyEndRestIsCalled_InformationToShowIsChanged(self):
        message = 'message'
        window = MainWindow()
        window.notifyStopRest(message)
        self.assertEqual(window.informationToShow, message)


    def test_calculateTimeLeft_25MinTotalnoElapsedTime_25MinTimeLeft(self):
        window = MainWindow()
        window.initialize(25,5)
        window.isWorkTime = True
        elapsedTime = timedelta(seconds=0)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=25))


    def test_calculateTimeLeft_25MinTotalOneMinuteElapsedTime_24MinTimeLeft(self):
        window = MainWindow()
        window.initialize(25,5)
        window.isWorkTime = True
        elapsedTime = timedelta(minutes=1)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=24))


    def test_calculateTimeLeft_25MinTotal25MinElapsed_0MinTimeLeft(self):
        window = MainWindow()
        window.initialize(25,5)
        window.isWorkTime = True
        elapsedTime = timedelta(minutes=25)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=0))


    def test_calculateTimeLeft_25MinTotal25Min1SecElapsed_0MinTimeLeft(self):
        window = MainWindow()
        window.initialize(25,5)
        window.isWorkTime = True
        elapsedTime = timedelta(minutes=25, seconds = 1)
        timeLeft = window.calculateTimeLeft(elapsedTime)
        self.assertEqual(timeLeft, timedelta(minutes=0))


    def test_getTimeUsed_isWorkTime_returns25(self):
        window = MainWindow()
        window.initialize(25,5)
        window.isWorkTime = True
        timeUsed = window.getTimeUsed()
        self.assertEqual(timeUsed, 25)


    def test_getTimeUsed_isNotWorkTime_returns5(self):
        window = MainWindow()
        window.initialize(25,5)
        window.isWorkTime = False
        timeUsed = window.getTimeUsed()
        self.assertEqual(timeUsed, 5)


