import unittest
from pomattack.logic.basicLogic import PomodoroTimer

class BasicLogicTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_PomodoroTimer_NoSubscriptions_ShouldEnd(self):
        timer = PomodoroTimer(0.001, 0.001)
        timer.startWork()
        self.assertTrue(True)

    def test_PomodoroTimer_SubscriptionAdded_SubscriptionIsCalled(self):
        timer = PomodoroTimer(0.001. 0.001)
        timer.startWork()



if __name__ == '__main__':
    unittest.main()
