import unittest
import sys
from mock import Mock
from pomattack.logic.basicLogic import PomodoroTimer
import time


class BasicLogicTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_PomodoroTimer_NoSubscriptions_ShouldEnd(self):
        timer = PomodoroTimer(0, 0)
        timer.startWork()
        self.assertTrue(True)

    def test_PomodoroTimer_SubscriptionAdded_SubscriptionIsCalled(self):
        timer = PomodoroTimer(0, 0)
        mockListener = Mock()
        timer.addListener(mockListener)
        timer.startWork()
        time.sleep(0.05)
        self.assertTrue(mockListener.notifyEnd.call_count == 2)

    def test_addListener_removeListener_ListernetIsAdded(self):
        timer = PomodoroTimer(0, 0)
        listener = Listener()
        self.assertTrue(len(timer.stopEvent) == 0)
        timer.addListener(listener)
        self.assertTrue(len(timer.stopEvent) == 1)
        timer.removeListener(listener)
        self.assertTrue(len(timer.stopEvent) == 0)


class Listener:
    def notifyEnd(message):
        pass


if __name__ == '__main__':
    unittest.main()
