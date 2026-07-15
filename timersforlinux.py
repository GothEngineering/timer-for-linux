import customtkinter
import tkinter
import time

root = customtkinter.CTk()
root.title("Timer")
root.geometry("400x400")
root.config(bg="gray20") # Find a more pretty colour please, this gray looks a little too intense
# Remember you have to change the background of each label and button to the same colour so it doesn't clash with the real bg

class Timer:
    counting_down = False
    text_input = tkinter.StringVar()
    
    def __init__(self):
        self.label_test = customtkinter.CTkLabel(root, text=f"Timer", text_color="white", fg_color="black")
        self.label_test.pack(fill="both")
        
        self.button_test = customtkinter.CTkButton(root, text="Start", text_color="white", fg_color="black", command=self.countdown_start)
        self.button_test.pack(side="bottom")

        
        self.timer_input = customtkinter.CTkEntry(root, textvariable = self.text_input, font=("calibre", 15, "normal"))
        self.timer_input.pack()
        
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
        self.counting_timer()
        
        # This part right here turns the input into the time I desire (for example 15 minutes)
        # TO DO: make it show a template of 00:00:00, read more about the tkinter entries later
        # It should use that string and turn it into the timer "time" like a pomodoro thingie
        user_time = self.timer_input.get()
        print(f"Timer time test: {user_time}")
        self.timer_input.set("")

    # Change the function to a constant loop that tracks the timer, it should ring when finished. The start button simply tracks the beginning
    # It shouldn't also tell the final part
    def counting_timer(self):
        if self.counting_down == False:
            end_time = time.time()
            #final_time = end_time - self.start_time
            #print(f"Segundos pasados: {final_time}")


   


timer = Timer()
root.mainloop()
