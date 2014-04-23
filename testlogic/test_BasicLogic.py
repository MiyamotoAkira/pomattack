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
        timer.addStartWorkListener(mockListener)
        timer.addStopWorkListener(mockListener)
        timer.addStartRestListener(mockListener)
        timer.addStopRestListener(mockListener)
        timer.startWork()
        time.sleep(0.05)
        self.assertTrue(mockListener.notifyStopWork.call_count == 1)
        self.assertTrue(mockListener.notifyStartWork.call_count == 1)
        self.assertTrue(mockListener.notifyStartRest.call_count == 1)
        self.assertTrue(mockListener.notifyStopRest.call_count == 1)


    def test_PomodoroTimer_AllSubscriptionsAdded_AllSubscriptionsAreCalled(self):
        timer = PomodoroTimer(0, 0)
        mockListener = Mock()
        timer.addAllListeners(mockListener)
        timer.startWork()
        time.sleep(0.05)
        self.assertTrue(mockListener.notifyStopWork.call_count == 1)
        self.assertTrue(mockListener.notifyStartWork.call_count == 1)
        self.assertTrue(mockListener.notifyStartRest.call_count == 1)
        self.assertTrue(mockListener.notifyStopRest.call_count == 1)


    def test_PomodoroTimer_StopWorkWithStartRest_SubscriptionIsCalled(self):
        timer = PomodoroTimer(0, 0)
        mockListener = Mock()
        timer.addStopWorkListener(mockListener)
        timer.addStartRestListener(mockListener)
        timer.stopWork()
        time.sleep(0.05)
        self.assertTrue(mockListener.notifyStopWork.call_count == 1)
        self.assertTrue(mockListener.notifyStartRest.call_count == 1)


    def test_PomodoroTimer_StopWorkWithoutStartRest_SubscriptionIsCalled(self):
        timer = PomodoroTimer(0, 0)
        mockListener = Mock()
        timer.addStopWorkListener(mockListener)
        timer.addStartRestListener(mockListener)
        timer.stopWork(False)
        time.sleep(0.05)
        self.assertTrue(mockListener.notifyStopWork.call_count == 1)
        self.assertTrue(mockListener.notifyStartRest.call_count == 0)


    def test_addStopWorkListener_removeStopWorkListenerListener_ListernetIsAdded(self):
        timer = PomodoroTimer(0, 0)
        listener = Listener()
        self.assertTrue(len(timer.stopWorkEvent) == 0)
        timer.addStopWorkListener(listener)
        self.assertTrue(len(timer.stopWorkEvent) == 1)
        timer.removeStopWorkListener(listener)
        self.assertTrue(len(timer.stopWorkEvent) == 0)


class Listener:
    def notifyEnd(message):
        pass


if __name__ == '__main__':
    unittest.main()
