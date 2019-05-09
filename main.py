import tkinter as tk
from tkinter import Button, Canvas, Frame, LEFT, BOTTOM

class DfaScreen():
    #decouple logic from code
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.build_ui()

        self.current_mode = "Start"
        self.number_of_states = 0
        
    
    def build_ui(self):
        self.add_title()
        self.add_quit_button()
        self.add_nav_buttons()
        self.add_canvas()
        self.upload_dfa_as_file()

    def add_title(self):
        label = tk.Label(self.frame, text="PFLAP ~ DFA")
        label.pack(side="top", fill="x", pady=10)

    def add_quit_button(self):
        self.button = Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)

    def add_nav_buttons(self):
        MODES = [
            ("Add State",  self.set_add_state_mode),
            ("Add Transition Arrow", self.set_add_transition_mode),
            ("Delete State",  self.set_delete_mode),
            ("Edit State",self.set_edit_state_mode),
        ]

        for text, command in MODES:
            self.button = Button(
                self.frame, text=text, fg="black", command=command
            )
            self.button.pack(side=LEFT)

    def set_add_state_mode(self):
        self.current_mode = "ADD_STATE"

    def set_add_transition_mode(self):
        self.current_mode = "ADD_TRANSITION"

    def set_delete_mode(self):
        self.current_mode = "DELETE_STATE"

    def set_edit_state_mode(self):
        self.current_mode = "EDIT_STATE"

    def add_canvas(self):
        self.canvas = Canvas(root, width=400, height=400)
        self.canvas.configure(background='grey')
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.bind("<ButtonRelease>", self.on_release)
        self.canvas.pack()
    
    def callback(self, event):
        if self.current_mode == "ADD_STATE":
            self.add_state(event)
        elif self.current_mode == "ADD_TRANSITION":
            self.add_transition(event)
        elif self.current_mode == "DELETE_STATE":
            self.delete_state(event)
        elif self.current_mode == "EDIT_STATE":
            self.edit_state(event)
        print("clicked at", self.current_mode, event.x, event.y)
    
    def add_state(self, event):
        x_coord_clicked = event.x
        y_coord_clicked = event.y

        #I wanted to make the radius of the circle 25
        x0 = x_coord_clicked - 25
        x1 = x_coord_clicked + 25

        y0 = y_coord_clicked + 25
        y1 = y_coord_clicked - 25

        state_id = self.canvas.create_oval(
            x0, y0, x1, y1, fill="yellow", tags=str(self.number_of_states))

        state_title = self.get_state_title()

        self.canvas.create_text(x_coord_clicked, y_coord_clicked, fill="black", font="Times 18 italic bold",
                                text=state_title)
        
    
    def get_state_title(self):
        next_unique_state_number = self.number_of_states
        next_unique_state_number = str(next_unique_state_number)
        next_unique_state_number = "q" + next_unique_state_number
        self.number_of_states += 1
        return next_unique_state_number

    
    def add_transition(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        closest_item_tag = self.canvas.find_closest(
             x, y, halo=None, start=None)[0]
        
        print("in add transition mode")
    
    def delete_state(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        closest_item_tag = self.canvas.find_closest(x, y, halo=None, start=None)[0]
        self.canvas.delete(closest_item_tag)
    
    def edit_state(self, event):
        pass
    def on_release(self, event):
        #add transition arrow
        if self.current_mode == "ADD_TRANSITION":
            print("mouse released", event.x, event.y)
        else:
            return

    def upload_dfa_as_file(self):
        self.button = Button(
            self.frame, text="Create DFA From File", fg="black", command=self.upload_file)
        self.button.pack(side=BOTTOM)
    
    def upload_file(self):
        print("get file")


if __name__ == "__main__":
    root = tk.Tk()
    app = DfaScreen(root)
    root.mainloop()
