import customtkinter
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import datetime

color_palette = {
    "background_color": "#212529",
    "label_color": "#212529",
    "arc_color": "#89b4fa",
    "button_color": "#343a40",
    "color_of_text": "#e2e8f0",
}


root = customtkinter.CTk()
root.title("Timer for Linux v2.0") # Is this name even accurate if it has a Windows version?
root.geometry("420x415")
# Remember you have to change the background of each label and button to the same colour so it doesn't clash with the real bg

# Find the notification sound when running the executable (or from the terminal)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Timer:

    def __init__(self):
        root.config(bg=color_palette["background_color"])
        pygame.mixer.init()
        self.counting_down = False
        self.is_running = False
        self.hours_placeholder = "00"
        self.minutes_placeholder = "00"
        self.seconds_placeholder = "00"  
        self.current_seconds = 0
        

        # That little timer text on top of the timer arc
        self.label_text = customtkinter.CTkLabel(root, text="00:00:00", 
        text_color=color_palette["color_of_text"], 
        bg_color=color_palette["label_color"], font=("calibre", 30, "normal"))
        self.label_text.grid(row=2, column=1, columnspan=3, sticky="nsew")

        # The start button
        self.start_button = customtkinter.CTkButton(root, text="Start", 
        text_color=color_palette["color_of_text"], 
        fg_color=color_palette["button_color"], command=self.countdown_start, 
        bg_color=color_palette["background_color"])
        self.start_button.grid(row=4, column=2, sticky="nsew")
        
        # The pause button
        self.pause_button = customtkinter.CTkButton(root, text="Pause", 
        text_color=color_palette["color_of_text"], 
        fg_color=color_palette["button_color"], bg_color=color_palette["background_color"],
        command=self.pause_timer)
        self.pause_button.grid(row=4, column=3, sticky="nsew")

        # The reset button
        self.reset_button = customtkinter.CTkButton(root, text="Reset Timer", 
        text_color=color_palette["color_of_text"], 
        fg_color=color_palette["button_color"], bg_color=color_palette["background_color"],
        command=self.reset_timer)
        self.reset_button.grid(row=4, column=1, sticky="nsew")

        # Hours, minutes and seconds
        self.hours_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), 
        bg_color=color_palette["background_color"],
        placeholder_text="Hours", placeholder_text_color="gray50", justify="center")
        self.hours_input.grid(row=1, column=1, sticky="ew")
        
        self.minutes_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), 
        bg_color=color_palette["background_color"],
        placeholder_text="Minutes", placeholder_text_color="gray50", justify="center")
        self.minutes_input.grid(row=1, column=2, sticky="nsew")
        
        self.seconds_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), 
        bg_color=color_palette["background_color"],
        placeholder_text="Seconds", placeholder_text_color="gray50", justify="center")
        self.seconds_input.grid(row=1, column=3, sticky="nsew")

        
        # TO DO: Find a way to show the theme selected, right now the init function is
        # overwritting the combobox that says which theme is on right now
        self.colour_button = customtkinter.CTkComboBox(root, 
        values=["Default", "Purple", "Black", "Amber",], 
        command=self.changing_colour, bg_color=color_palette["background_color"],
        
        )
        self.colour_button.grid(row=5, column=2)


        # The canvas creation, for now it doesn't expand alongside the window
        self.timer_circle = customtkinter.CTkCanvas(root, height=300, width=300, 
        bg=color_palette["background_color"], highlightbackground=color_palette["background_color"])

                                                      #X1, Y1, X2, Y2. That's the coordinates of each number
        self.pie_chart = self.timer_circle.create_arc(110, 50, 310, 250, start=90, extent=359.9, width=15, 
        outline=color_palette["arc_color"], style="arc")
        self.timer_circle.grid(row=3, column=1, columnspan=3, sticky="nsew")
        # Remember, X1 and Y1 are the starting point of the rectangle, X2 and Y2 are the finish point. Because I wanted the arc to be centered
        # I substracted the first and the latter Y's by half the amount of the width and height (supposedly but it works now atleast)
    
        root.columnconfigure(2, weight=1)
        root.rowconfigure(2, weight=1)

    # To do: add a pop up instead of silently cancelling the function to avoid users from
    # thinking the app is broken when changing the theme mid countdown
    def changing_colour(self, choice):
        if self.is_running:
            return

        if choice == "Default":
            color_palette["background_color"] = "#212529"
            color_palette["label_color"] = "#212529"
            color_palette["arc_color"] = "#89b4fa"
            color_palette["button_color"] = "#343a40"
            color_palette["color_of_text"] = "#e2e8f0"
            self.__init__()


        elif choice == "Purple":
            color_palette["background_color"] = "#1E1E1E"
            color_palette["label_color"] = "#1E1E1E"
            color_palette["arc_color"] = "#B0B0B0"
            color_palette["button_color"] = "#3a1c42"
            color_palette["color_of_text"] = "#f3e8ff"
            self.__init__()
            

        elif choice == "Black":
            color_palette["background_color"] = "#0a0a0a"
            color_palette["label_color"] = "#161616"
            color_palette["arc_color"] = "#8b0000"
            color_palette["button_color"] = "#161616"
            color_palette["color_of_text"] = "#e5e7eb"
            self.__init__()


        elif choice == "Amber":
            color_palette["background_color"] = "#1a1816"
            color_palette["label_color"] = "#2a2622"
            color_palette["arc_color"] = "#ffb703"
            color_palette["button_color"] = "#3d3732"
            color_palette["color_of_text"] = "#f5f2eb"
            self.__init__()


        else:
            print("Error D:")

    def countdown_start(self):

        if self.is_running:
            return

        else:
        
        
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

            self.timer_id = root.after(1000, self.counting_timer)

    def pause_timer(self):

        if self.current_seconds == 0:
            return
        else:

            if self.counting_down:
                self.pause_button.configure(text="Unpause")

            else:
                self.pause_button.configure(text="Pause")

            self.counting_down = not self.counting_down
            
            self.counting_timer()

    
    def reset_timer(self):

        root.after_cancel(self.timer_id)
        self.current_seconds = 0
        self.timer_circle.itemconfig(self.pie_chart, extent=359.9)
        self.total_seconds = 0
        self.is_running = False
        self.counting_down = False
        self.label_text.configure(text="00:00:00")
        
        
    # The credits are to universfield tyvm
    def timer_finished(self):
        notification_file = resource_path("universfield-notif.ogg")
        alarm_noise = pygame.mixer.Sound(notification_file)
        alarm_noise.play(loops=4)


timer = Timer()
root.mainloop()
