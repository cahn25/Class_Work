class Motor:
    def __init__(self): #method
        self.speed = 0.5 #set to 0 so it doesn't turn on from the start
    def set_speed(self, newSpeed):
        self.speed = newSpeed
    def speed_up(self):
        self.speed = self.speed * 2 #property
    def slow_down(self):
        self.speed = self.speed * 0.5



