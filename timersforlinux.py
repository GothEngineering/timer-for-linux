import customtkinter
import tkinter
import time

root = customtkinter.CTk()
root.title("Timer")
root.geometry("400x300")

class Timer:
    def __init__(self):
        self.label_test = customtkinter.CTkLabel(root, text=f"Timer", text_color="white", fg_color="black")
        self.label_test.pack(fill="both")
        


        self.timer_circle = customtkinter.CTkCanvas(root, height=400, width=300, bg="gray")
        self.timer_circle.pack(expand=True, fill="both")
                                                      #X1, Y1, X2, Y2. That's the coordinates of each number
        self.pie_chart = self.timer_circle.create_arc(100, 40, 300, 240, start=90, extent=359.9, width=10, outline="red", style="arc")
        # Remember, X1 and Y1 are the starting point of the rectangle, X2 and Y2 are the finish point. Because I wanted the arc to be centered
        # I substracted the first and the latter Y's by half the amount of the width and height (supposedly but it works now atleast)
        

   


timer = Timer()
root.mainloop()
