import customtkinter
import pygame
import timer_logic
import main

color_palette = {
    "background_color": "#212529",
    "label_color": "#212529",
    "arc_color": "#89b4fa",
    "button_color": "#343a40",
    "color_of_text": "#e2e8f0",
}


class TimerUI:
    # fix this mess tomorrow lol
    def __init__(self):
        main.root.config(bg=color_palette["background_color"])
        pygame.mixer.init()


        # That little timer text on top of the timer arc
        self.label_text = customtkinter.CTkLabel(main.root, text="00:00:00", 
        text_color=color_palette["color_of_text"], 
        bg_color=color_palette["label_color"], font=("calibre", 30, "normal"))
        self.label_text.grid(row=2, column=1, columnspan=3, sticky="nsew")

        # The start button
        self.start_button = customtkinter.CTkButton(main.root, text="Start", 
        text_color=color_palette["color_of_text"], 
        fg_color=color_palette["button_color"], command=self.countdown_start, 
        bg_color=color_palette["background_color"])
        self.start_button.grid(row=4, column=2, sticky="nsew")
        
        # The pause button
        self.pause_button = customtkinter.CTkButton(main.root, text="Pause", 
        text_color=color_palette["color_of_text"], 
        fg_color=color_palette["button_color"], bg_color=color_palette["background_color"],
        command=self.pause_timer)
        self.pause_button.grid(row=4, column=3, sticky="nsew")

        # The reset button
        self.reset_button = customtkinter.CTkButton(main.root, text="Reset Timer", 
        text_color=color_palette["color_of_text"], 
        fg_color=color_palette["button_color"], bg_color=color_palette["background_color"],
        command=self.reset_timer)
        self.reset_button.grid(row=4, column=1, sticky="nsew")

        # Hours, minutes and seconds
        self.hours_input = customtkinter.CTkEntry(main.root, font=("calibre", 15, "normal"), 
        bg_color=color_palette["background_color"],
        placeholder_text="Hours", placeholder_text_color="gray50", justify="center")
        self.hours_input.grid(row=1, column=1, sticky="ew")
        
        self.minutes_input = customtkinter.CTkEntry(main.root, font=("calibre", 15, "normal"), 
        bg_color=color_palette["background_color"],
        placeholder_text="Minutes", placeholder_text_color="gray50", justify="center")
        self.minutes_input.grid(row=1, column=2, sticky="nsew")
        
        self.seconds_input = customtkinter.CTkEntry(main.root, font=("calibre", 15, "normal"), 
        bg_color=color_palette["background_color"],
        placeholder_text="Seconds", placeholder_text_color="gray50", justify="center")
        self.seconds_input.grid(row=1, column=3, sticky="nsew")

        
        # TO DO: Find a way to show the theme selected, right now the init function is
        # overwritting the combobox that says which theme is on right now
        self.colour_button = customtkinter.CTkComboBox(main.root, 
        values=["Default", "Purple", "Black", "Amber",], 
        command=self.changing_colour, bg_color=color_palette["background_color"],
        
        )
        self.colour_button.grid(row=5, column=2)


        # The canvas creation, for now it doesn't expand alongside the window
        self.timer_circle = customtkinter.CTkCanvas(main.root, height=300, width=300, 
        bg=color_palette["background_color"], highlightbackground=color_palette["background_color"])

                                                      #X1, Y1, X2, Y2. That's the coordinates of each number
        self.pie_chart = self.timer_circle.create_arc(110, 50, 310, 250, start=90, extent=359.9, width=15, 
        outline=color_palette["arc_color"], style="arc")
        self.timer_circle.grid(row=3, column=1, columnspan=3, sticky="nsew")
        # Remember, X1 and Y1 are the starting point of the rectangle, X2 and Y2 are the finish point. Because I wanted the arc to be centered
        # I substracted the first and the latter Y's by half the amount of the width and height (supposedly but it works now atleast)
    
        main.root.columnconfigure(2, weight=1)
        main.root.rowconfigure(2, weight=1)

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

        main.root.after_cancel(self.timer_id)
        self.current_seconds = 0
        self.timer_circle.itemconfig(self.pie_chart, extent=359.9)
        self.total_seconds = 0
        self.is_running = False
        self.counting_down = False
        self.label_text.configure(text="00:00:00")