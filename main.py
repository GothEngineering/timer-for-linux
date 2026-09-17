print("Opening main")
import customtkinter
import timer_ui

def main():
    root = customtkinter.CTk()
    root.title("Timer for Linux v3.0") # Is this name even accurate if it has a Windows version?
    root.geometry("420x415")
    app = timer_ui.TimerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()