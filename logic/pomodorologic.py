class Pomodoro():
    '''This class handles the logic of a pomodoro timer'''
    def __init__(self, workTime=0, restTime=0):
        '''workTime and restTime are the values used for the timer.
        They are indicated in seconds'''
        self.workTime = workTime
        self.restTime = restTime
