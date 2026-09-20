
class TimerLogic:

    def countdown_start(self, h, m, s):
        self.current_seconds = 0

        # Math to get the total amount of time with every input
        hours = h
        minutes = m
        seconds = s

        total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
        self.current_seconds = total_seconds
        if self.current_seconds != 0:
            self.current_seconds += 1

        return self.current_seconds