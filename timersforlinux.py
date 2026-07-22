import customtkinter
import tkinter
import time

root = customtkinter.CTk()
root.title("Timer")
root.geometry("420x360")
root.config(bg="gray20") # Find a more pretty colour please, this gray looks a little too intense
# Remember you have to change the background of each label and button to the same colour so it doesn't clash with the real bg

class Timer:

    def __init__(self):
        self.counting_down = False
        self.hours_placeholder = "00"
        self.minutes_placeholder = "00"
        self.seconds_placeholder = "00"  

        
        self.button_test = customtkinter.CTkButton(root, text="Start", text_color="white", fg_color="black", command=self.countdown_start, 
        bg_color="gray20")
        self.button_test.grid(row=3, column=2)
        

        self.hours_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color="gray20",
        placeholder_text="Hours", placeholder_text_color="gray50", justify="center")
        self.hours_input.grid(row=1, column=1)
        
        
        self.minutes_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color="gray20",
        placeholder_text="Minutes", placeholder_text_color="gray50", justify="center")
        self.minutes_input.grid(row=1, column=2)
        
        
        self.seconds_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color="gray20",
        placeholder_text="Seconds", placeholder_text_color="gray50", justify="center")
        self.seconds_input.grid(row=1, column=3)
        
        
        self.timer_circle = customtkinter.CTkCanvas(root, height=300, width=300, bg="gray30")
        
                                                      #X1, Y1, X2, Y2. That's the coordinates of each number
        self.pie_chart = self.timer_circle.create_arc(50, 30, 250, 230, start=90, extent=359.9, width=10, outline="red", style="arc")
        self.timer_circle.grid(row=2, column=1, columnspan=3)
        # Remember, X1 and Y1 are the starting point of the rectangle, X2 and Y2 are the finish point. Because I wanted the arc to be centered
        # I substracted the first and the latter Y's by half the amount of the width and height (supposedly but it works now atleast)
    
        #root.columnconfigure(0, weight=1)
        #root.rowconfigure(0, weight=1)
    
    def countdown_start(self):
        self.start_time = time.time()
        self.counting_down = not self.counting_down
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
    
        self.counting_timer()

    
    
    def counting_timer(self):
        
        #hours = self.hours_entry
        #minutes = self.minutes_entry
        #seconds = self.seconds_entry

        #self.total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
        #print(f"tiempo total papu: {self.total_seconds}")
        
        if self.total_seconds > 0:
            self.total_seconds -= 1
            print(f"Ticking down... {self.total_seconds}")
            
            if self.total_seconds == 0:
                print("YIPPIEEE")
            
            root.after(1000, self.counting_timer)

        

        
        
        



timer = Timer()
root.mainloop()
