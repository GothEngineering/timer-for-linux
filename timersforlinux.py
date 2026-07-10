import customtkinter
import tkinter
import time

root = customtkinter.CTk()
root.title("Timer")
root.geometry("400x300")


label_test = customtkinter.CTkLabel(root, text="Test insano", text_color="BLACK")
label_test.pack()

canvas = customtkinter.CTkCanvas(root, width=200, height=200)
canvas.pack()

canvas.create_aa_circle(100, 100, 60)


root.mainloop()
