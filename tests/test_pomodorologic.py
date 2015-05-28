import unittest
import time
import mock
from nose_parameterized import parameterized
from logic import pomodorologic
from pubsub import pub

class TestSetup(unittest.TestCase):
    def test_set_pomodoro_timer_on_constructor(self):
        workTime = 25
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        self.assertEqual(pomodoro.workTime, workTime)
        self.assertEqual(pomodoro.restTime, restTime)

    def test_not_set_pomodoro_timer_on_constructor(self):
        pomodoro = pomodorologic.Pomodoro()
        self.assertEqual(pomodoro.workTime, 0)
        self.assertEqual(pomodoro.restTime, 0)

    def test_set_pomodoro_timer_on_members(self):
        workTime = 25
        restTime = 5
        pomodoro = pomodorologic.Pomodoro()
        pomodoro.workTime = workTime
        pomodoro.restTime = restTime
        self.assertEqual(pomodoro.workTime, workTime)
        self.assertEqual(pomodoro.restTime, restTime)

    def test_raise_event_onEndOfWork(self):
        workTime = 0.1
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        mocked = mock. Mock()
        pub.subscribe(mocked, 'onEndOfWork')
        pomodoro.startWork()
        time.sleep(0.2)
        self.assertTrue(mocked.called)
        pub.unsubscribe(mocked, 'onEndOfWork')

    def test_raise_event_OnStartOfWork(self):
        workTime = 0.1
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        mocked = mock.Mock()
        pub.subscribe(mocked, 'onStartOfWork')
        pomodoro.startWork()
        self.assertTrue(mocked)
        pub.unsubscribe(mocked, 'onStartOfWork')

    def test_raise_event_onEndOfRest(self):
        workTime = 0.1
        restTime = 0.1
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        mocked = mock. Mock()
        pub.subscribe(mocked, 'onEndOfRest')
        pomodoro.startRest()
        time.sleep(0.2)
        self.assertTrue(mocked.called)
        pub.unsubscribe(mocked, 'onEndOfRest')

    def test_raise_event_OnStartOfRest(self):
        workTime = 0.1
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        mocked = mock.Mock()
        pub.subscribe(mocked, 'onStartOfRest')
        pomodoro.startRest()
        self.assertTrue(mocked)
        pub.unsubscribe(mocked, 'onStartOfRest')

    def test_cancel_work(self):
        workTime = 5
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        mockCancel = mock.Mock()
        mockEnd = mock.Mock()
        pub.subscribe(mockCancel, 'onCancelWork')
        pub.subscribe(mockEnd, 'onEndOfWork')
        pomodoro.startWork()
        pomodoro.cancelWork()
        self.assertTrue(mockCancel.called)
        self.assertTrue(mockEnd.called)

    def test_cancel_rest(self):
        workTime = 5
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        mockCancel = mock.Mock()
        mockEnd = mock.Mock()
        pub.subscribe(mockCancel, 'onCancelRest')
        pub.subscribe(mockEnd, 'onEndOfRest')
        pomodoro.startRest()
        pomodoro.cancelRest()
        self.assertTrue(mockCancel.called)
        self.assertTrue(mockEnd.called)

    def test_cancel_work_without_starting(self):
        workTime = 5
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        try:
            pomodoro.cancelWork()
        except:
            self.fail("Error was thrown")

    def test_cancel_rest_without_starting(self):
        workTime = 5
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        try:
            pomodoro.cancelRest()
        except:
            self.fail("Error was thrown")

    def test_do_a_pomodoro(self):
        workTime = 0.1
        restTime = 0.1
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        mockStartWork = mock.Mock()
        mockEndWork = mock.Mock()
        mockStartRest = mock.Mock()
        mockEndRest = mock.Mock()
        pub.subscribe(mockStartWork, 'onStartOfWork')
        pub.subscribe(mockEndWork, 'onEndOfWork')
        pub.subscribe(mockStartRest, 'onStartOfRest')
        pub.subscribe(mockEndRest, 'onEndOfRest')
        pomodoro.DoPomodoros(1)
        time.sleep(0.3)
        self.assertTrue(mockStartWork.called)
        self.assertTrue(mockEndWork.called)
        self.assertTrue(mockStartRest.called)
        self.assertTrue(mockEndRest.called)
        
        
