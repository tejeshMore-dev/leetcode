class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append((startTime, 1))
            self.events.append((endTime, -1))
            return True
        
        bookings = 0
        previous = self.events[0][0]

        for position, change in self.events:
            overlap =  max(previous, startTime) < min(position, endTime)

            if overlap and bookings == 1:
                return False
            
            bookings += change
            previous = position
            
        insort(self.events, (startTime, 1))
        insort(self.events, (endTime, -1))

        return True

        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)