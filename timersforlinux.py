import customtkinter
import tkinter
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

# Timer colors
background_color = "#212529"
label_color = "#212529"
arc_color = "#89b4fa"
button_color = "#343a40"


root = customtkinter.CTk()
root.title("Timer for Linux")
# Reminder: X and Y
root.geometry("420x415")
root.config(bg=background_color)
# Remember you have to change the background of each label and button to the same colour so it doesn't clash with the real bg


class Timer:

    def __init__(self):
        pygame.mixer.init()
        self.counting_down = False
        self.is_running = False
        self.hours_placeholder = "00"
        self.minutes_placeholder = "00"
        self.seconds_placeholder = "00"  
        self.current_seconds = 0
        

        # That little timer on top of the timer
        self.label_text = customtkinter.CTkLabel(root, text="00:00:00", text_color="white", bg_color=label_color, font=("calibre", 30, "normal"))
        self.label_text.grid(row=2, column=1, columnspan=3, sticky="nsew")

        # The start button
        self.start_button = customtkinter.CTkButton(root, text="Start", text_color="white", fg_color=button_color, command=self.countdown_start, 
        bg_color=background_color)
        self.start_button.grid(row=4, column=2, sticky="nsew")
        
        # The pause button
        self.pause_button = customtkinter.CTkButton(root, text="Pause", text_color="white", fg_color=button_color, bg_color=background_color,
        command=self.pause_timer)
        self.pause_button.grid(row=4, column=3, sticky="nsew")

        # The reset button
        self.reset_button = customtkinter.CTkButton(root, text="Reset Timer", text_color="white", fg_color=button_color, bg_color=background_color,
        command=self.reset_timer)
        self.reset_button.grid(row=4, column=1, sticky="nsew")

        # Hours, minutes and seconds
        self.hours_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color=background_color,
        placeholder_text="Hours", placeholder_text_color="gray50", justify="center") # Change the background color here
        self.hours_input.grid(row=1, column=1, sticky="ew")
        
        self.minutes_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color=background_color,
        placeholder_text="Minutes", placeholder_text_color="gray50", justify="center")
        self.minutes_input.grid(row=1, column=2, sticky="nsew")
        
        self.seconds_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color=background_color,
        placeholder_text="Seconds", placeholder_text_color="gray50", justify="center")
        self.seconds_input.grid(row=1, column=3, sticky="nsew")
        
        
        # The canvas creation, for now it doesn't expand alongside the window
        self.timer_circle = customtkinter.CTkCanvas(root, height=300, width=300, bg=background_color, highlightbackground=background_color)

                                                      #X1, Y1, X2, Y2. That's the coordinates of each number
        self.pie_chart = self.timer_circle.create_arc(110, 50, 310, 250, start=90, extent=359.9, width=15, outline=arc_color, style="arc")
        self.timer_circle.grid(row=3, column=1, columnspan=3, sticky="nsew")
        # Remember, X1 and Y1 are the starting point of the rectangle, X2 and Y2 are the finish point. Because I wanted the arc to be centered
        # I substracted the first and the latter Y's by half the amount of the width and height (supposedly but it works now atleast)
    
        root.columnconfigure(2, weight=1)
        root.rowconfigure(2, weight=1)
    
    def countdown_start(self):

        if self.is_running:
            print(f"Oli, no puedes iniciar otro timer ahorita ya que is_running es: {self.is_running}")
            return

        else:
            
            print(f"La variable al activar es: {self.counting_down}")
        
        
            # This part right here turns the input into the time I desire (for example 15 minutes)
            self.hours_entry = self.hours_input.get()
            self.minutes_entry = self.minutes_input.get()
            self.seconds_entry = self.seconds_input.get()
        
            # Remember: Left variable = Right variable
            # Right variable overwrites the left variable, right variable stays the same. Right assigns to Left
            if self.hours_entry == "":
                self.hours_entry = self.hours_placeholder
            else:
                self.hours_entry = self.hours_entry
        
        
            if self.minutes_entry == "":
                self.minutes_entry = self.minutes_placeholder
            else:
                self.minutes_entry = self.minutes_entry
        
        
            if self.seconds_entry == "":
                self.seconds_entry = self.seconds_placeholder
            else:
                self.seconds_entry = self.seconds_entry
        
            self.hours_input.set("")
            self.minutes_input.set("")
            self.seconds_input.set("")
            print(f"Timer time test: {self.hours_entry}:{self.minutes_entry}:{self.seconds_entry}")
    
            # Math to get the total amount of time with every input
            hours = self.hours_entry
            minutes = self.minutes_entry
            seconds = self.seconds_entry

            self.total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
            self.current_seconds = self.total_seconds

            # One second delay when starting
            self.current_seconds += 1

            if self.current_seconds > 1:
                self.counting_down = True
                self.is_running = True


            self.counting_timer()

    
    def counting_timer(self):

        if self.current_seconds > 0 and self.counting_down:
            self.current_seconds -= 1
            degrees = (self.current_seconds / self.total_seconds) * 359
            self.timer_circle.itemconfig(self.pie_chart, extent=degrees)
            print(f"Ticking down... {self.current_seconds}")

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
                self.current_seconds = 0
                print("YIPPIEEE")
                self.timer_circle.itemconfig(self.pie_chart, extent=359.9)
                self.is_running = False
                self.timer_finished()
                self.label_text.configure(text="Timer finished")

            self.timer_id = root.after(1000, self.counting_timer)

    def pause_timer(self):

        if self.current_seconds == 0:
            print("*no hace nada en python")
        else:

            if self.counting_down:
                self.pause_button.configure(text="Unpause")

            else:
                self.pause_button.configure(text="Pause")

            self.counting_down = not self.counting_down
            print(self.counting_down)
            self.counting_timer()

    
    def reset_timer(self):

        root.after_cancel(self.timer_id)
        self.current_seconds = 0
        self.timer_circle.itemconfig(self.pie_chart, extent=359.9)
        self.total_seconds = 0
        self.is_running = False
        self.counting_down = False
        self.label_text.configure(text="00:00:00")
        print("mreow timer stopped")
        
    # The credits are to universfield tyvm
    def timer_finished(self):
        alarm_noise = pygame.mixer.Sound("universfield-notification.ogg")
        alarm_noise.play(loops=3)


timer = Timer()
root.mainloop()
