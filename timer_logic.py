import main
import datetime

class TimerLogic:
    def countdown_start(self):
        self.counting_down = False
        is_running = False
        hours_placeholder = "00"
        minutes_placeholder = "00"
        seconds_placeholder = "00"  
        current_seconds = 0

        if is_running:
            return

        else:
        
        
        # This part right here turns the input into the time I desire (for example 15 minutes)
            hours_entry = hours_input.get()
            minutes_entry = minutes_input.get()
            seconds_entry = seconds_input.get()
        
        # Remember: Left variable = Right variable
        # Right variable overwrites the left variable, right variable stays the same. Right assigns to Left
            if hours_entry == "":
                hours_entry = hours_placeholder
            else:
                hours_entry = hours_entry
        
        
            if minutes_entry == "":
                minutes_entry = minutes_placeholder
            else:
                minutes_entry = minutes_entry
        
        
            if seconds_entry == "":
                seconds_entry = seconds_placeholder
            else:
                seconds_entry = seconds_entry
        
            hours_input.set("")
            minutes_input.set("")
            seconds_input.set("")
            
    
        # Math to get the total amount of time with every input
            hours = hours_entry
            minutes = minutes_entry
            seconds = seconds_entry

            total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
            current_seconds = total_seconds

            # One second delay when starting
            current_seconds += 1

            if current_seconds > 1:
                counting_down = True
                is_running = True


            self.counting_timer()

    
    def counting_timer(self):

        if self.current_seconds > 0 and self.counting_down:
            self.current_seconds -= 1

            # Arc logic to resize dynamically
            degrees = (self.current_seconds / self.total_seconds) * 359
            self.timer_circle.itemconfig(self.pie_chart, extent=degrees)
            

            # The math used to show the timer on the label
            self.timer_label = self.current_seconds
            hours_in_the_float = round(self.timer_label) // 3600
            seconds_without_hours = round(self.timer_label) % 3600
            minutes = seconds_without_hours // 60
            seconds_modulo = seconds_without_hours % 60

            self.label_template = f"{hours_in_the_float:02d}:{minutes:02d}:{seconds_modulo:02d}"
            self.label_text.configure(text=self.label_template)
            
            
            # Here's what happens when the timer is finished
            if self.current_seconds == 0:

                time_upon_finishing = datetime.datetime.now()
                # Just 24 hours time for now because I use it
                organized_time = time_upon_finishing.strftime("%H:%M")

                self.current_seconds = 0
                self.timer_circle.itemconfig(self.pie_chart, extent=359.9)
                self.is_running = False
                self.timer_finished()
                self.label_text.configure(text=f"Timer finished at {organized_time}")

            self.timer_id = main.root.after(1000, self.counting_timer)
