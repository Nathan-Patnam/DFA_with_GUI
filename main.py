import tkinter as tk
from tkinter import Button, Canvas, Frame, LEFT

class DFA():
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.current_mode = "Start"
        self.add_title()
        self.add_quit_button()
        self.add_nav_buttons()
        self.add_canvas()
        self.state = 0

    def add_title(self):
        label = tk.Label(self.frame, text="PFLAP")
        label.pack(side="top", fill="x", pady=10)

    def add_quit_button(self):
        self.button = Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)

    def add_nav_buttons(self):
        MODES = [
            ("Add State", "ADD_STATE", self.set_add_state_mode),
            ("Add Transition Arrow", "ADD_TRANSITION",
             self.set_add_transition_mode),
            ("Delete State", "DELETE_STATE", self.set_delete_mode),
            ("Edit State", "EDIT_STATE", self.set_edit_state_mode),
        ]

        for text, mode, command in MODES:
            self.button = Button(
                self.frame, text=text, fg="black", command=command
            )
            self.button.pack(side=LEFT)

    def set_add_state_mode(self):
        self.current_mode = "ADD_STATE"
        print("1")

    def set_add_transition_mode(self):
        self.current_mode = "ADD_TRANSITION"
        print("2")

    def set_delete_mode(self):
        self.current_mode = "DELETE_STATE"
        print("3")

    def set_edit_state_mode(self):
        self.current_mode = "EDIT_STATE"
        print("4")

    def add_canvas(self):
        self.canvas = Canvas(root, width=400, height=400)
        self.canvas.configure(background='grey')
        self.canvas.bind("<Button-1>", self.callback)
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
        print(event)
        x_coord_clicked = event.x
        y_coord_clicked = event.y

        x0 = x_coord_clicked - 25
        x1 = x_coord_clicked + 25

        y0 = y_coord_clicked + 25
        y1 = y_coord_clicked - 25

        state_id = self.canvas.create_oval(x0, y0, x1, y1, fill="yellow", tags=str(self.state))
        pass
    
    def add_transition(self, event):
        #draw an error from one state to another
        pass
    
    def delete_state(self, event):
        pass
    
    def edit_state(self, event):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = DFA(root)
    root.mainloop()
   
