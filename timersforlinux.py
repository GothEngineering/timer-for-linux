import customtkinter
import tkinter
import time

root = customtkinter.CTk()
root.title("Timer")
root.geometry("400x400")
root.config(bg="gray20") # Find a more pretty colour please, this gray looks a little too intense
# Remember you have to change the background of each label and button to the same colour so it doesn't clash with the real bg

class Timer:
    #counting_down = False
    #text_input = tkinter.StringVar()
      


    def __init__(self):
        self.counting_down = False
        self.hours_placeholder = "00"
        self.minutes_placeholder = "00"
        self.seconds_placeholder = "00"  
        self.hours_has_data = False
        self.minutes_has_data = False
        self.seconds_has_data = False
        
        
        #self.label_test = customtkinter.CTkLabel(root, text=f"Insert time below", text_color="white", fg_color="black")
        #self.label_test.pack(fill="both")
        
        self.button_test = customtkinter.CTkButton(root, text="Start", text_color="white", fg_color="black", command=self.countdown_start, 
        bg_color="gray20")
        self.button_test.pack(side="bottom")

        # TO DO: Change .pack() into .grid() so the buttons are horizontal
        self.hours_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color="gray20",
        placeholder_text="Hours", placeholder_text_color="gray50", justify="center")
        self.hours_input.pack()
        
        self.minutes_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color="gray20",
        placeholder_text="Minutes", placeholder_text_color="gray50", justify="center")
        self.minutes_input.pack()
        
        self.seconds_input = customtkinter.CTkEntry(root, font=("calibre", 15, "normal"), bg_color="gray20",
        placeholder_text="Seconds", placeholder_text_color="gray50", justify="center")
        self.seconds_input.pack()
        
        
        
        self.timer_circle = customtkinter.CTkCanvas(root, height=400, width=300, bg="gray30")
        self.timer_circle.pack(expand=True, fill="both")
                                                      #X1, Y1, X2, Y2. That's the coordinates of each number
        self.pie_chart = self.timer_circle.create_arc(100, 30, 300, 230, start=90, extent=359.9, width=10, outline="red", style="arc")
        
        # Remember, X1 and Y1 are the starting point of the rectangle, X2 and Y2 are the finish point. Because I wanted the arc to be centered
        # I substracted the first and the latter Y's by half the amount of the width and height (supposedly but it works now atleast)
    
    
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
            self.hours_has_data = False
        else:
            self.hours_entry = self.hours_entry
            self.hours_has_data = True
        
        
        if self.minutes_entry == "":
            self.minutes_entry = self.minutes_placeholder
            self.minutes_has_data = False
        else:
            self.minutes_entry = self.minutes_entry
            self.minutes_has_data = True
        
        
        if self.seconds_entry == "":
            self.seconds_entry = self.seconds_placeholder
            self.seconds_has_data = False
        else:
            self.seconds_entry = self.seconds_entry
            self.seconds_has_data = True
        
        self.hours_input.set("")
        self.minutes_input.set("")
        self.seconds_input.set("")
        print(f"Timer time test: {self.hours_entry}:{self.minutes_entry}:{self.seconds_entry}")
        print(f"Horas {self.hours_has_data}  | Minutos {self.minutes_has_data}  | Segundos {self.seconds_has_data}")
        self.counting_timer()

    # Change the function to a constant loop that tracks the timer, it should ring when finished. The start button simply tracks the beginning
    # it shouldn't also tell the final part
    def counting_timer(self):
        if self.hours_has_data == False and self.minutes_has_data == False and self.seconds_has_data == False:
            print("Error! please type something, dumbass")
        
        hours = self.hours_entry
        minutes = self.minutes_entry
        seconds = self.seconds_entry

        total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
            
        print(f"tiempo total papu: {total_seconds}")
        
        
        
        #if self.counting_down == False:
            #end_time = time.time()
            #final_time = end_time - self.start_time
            #print(f"Segundos pasados: {final_time}")


   


timer = Timer()
root.mainloop()
