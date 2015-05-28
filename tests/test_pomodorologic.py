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

    def method_call_check(self):
        self.called += 1

    def method_call_check2(self):
        self.called2 += 1

    def test_raise_event_onEndOfWork_over(self):
        workTime = 0.1
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        self.called = 0
        pub.subscribe(self.method_call_check, 'onEndOfWork')
        pomodoro.startWork()
        time.sleep(0.2)
        self.assertEqual(self.called, 1)
        pub.unsubscribe(self.method_call_check, 'onEndOfWork')

    def test_raise_event_OnStartOfWork(self):
        workTime = 0.1
        restTime = 5
        pomodoro = pomodorologic.Pomodoro(workTime, restTime)
        self.called2 = 0
        pub.subscribe(self.method_call_check2, 'onStartOfWork')
        pomodoro.startWork()
        self.assertEqual(self.called2, 1)
        pub.unsubscribe(self.method_call_check2, 'onStartOfWork')

