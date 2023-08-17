class Clock:
    def __init__(self) -> None:
        self.time = 0

    def advance(self,seconds: int) -> None:
        self.time += seconds
    
    def setTime(self, seconds: int) -> None:
        self.time = seconds