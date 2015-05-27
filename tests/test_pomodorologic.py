import unittest
from nose_parameterized import parameterized
from logic import pomodorologic

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
