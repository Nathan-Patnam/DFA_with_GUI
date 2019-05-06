import tkinter as tk
from tkinter import *


class App():
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.add_title()
        self.add_quit_button()
        self.add_nav_buttons()
        self.add_canvas()

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
            self.button  = Button(
                self.frame, text=text, fg="black", command=command
            )
            self.button.pack(side=LEFT)

    def set_add_state_mode(self):
        print("1")

    def set_add_transition_mode(self):
        print("2")

    def set_delete_mode(self):
        print("3")

    def set_edit_state_mode(self):
        print("4")


    def add_canvas(self):
        pass


    def add_create_dfa_button(self, controller):
        create_dfa = tk.Button(self, text="Create DFA",
                            command=lambda: controller.show_frame("CreateDFA"))
        create_dfa.pack()

    # class CreateDFA(tk.Frame):

    # def __init__(self, parent, controller):
    # tk.Frame.__init__(self, parent)
    # self.controller = controller
    # self.add_title(controller)
    # self.add_upload_dfa_from_file_button()
    # self.add_dfa_buttons(controller)
    # self.add_canvas(controller)
    # self.add_return_home_button()

    # def add_title(self, controller):
    # label = tk.Label(self, text="Create a DFA",
    #                  font=controller.title_font)
    # label.pack(side="top", fill="x", pady=10)

    # def add_dfa_buttons(self, controller):
    # MODES = [
    #     ("Add State", "ADD_STATE", self.set_add_state_mode),
    #     ("Add Transition Arrow", "ADD_TRANSITION",
    #      self.set_add_transition_mode),
    #     ("Delete State", "DELETE_STATE", self.set_delete_mode),
    #     ("Edit State", "EDIT_STATE", self.set_edit_state_mode),
    # ]
    # v = StringVar()
    # v.set("L")  # initialize

    # for text, mode, command in MODES:
    # b = Radiobutton(controller, text=text,
    #                 variable=v, value=mode, command=command)
    # b.pack(anchor="w")

    # def set_add_state_mode(self):
    # print("1")

    # def set_add_transition_mode(self):
    # print("2")

    # def set_delete_mode(self):
    # print("3")

    # def set_edit_state_mode(self):
    # print("4")

    # def add_upload_dfa_from_file_button(self):
    # file_button = tk.Button(self, text="Create DFA from file",
    #                         command=self.ask_for_file)
    # file_button.pack()

    # def add_canvas(self, controller):
    # canvas = Canvas(controller)

    # def add_return_home_button(self):
    # return_home_button = tk.Button(self, text="Go to the home page",
    #                                command=self.return_home)
    # return_home_button.pack()

    # def ask_for_file(self):
    # root = tk.Tk()
    # root.filename = filedialog.askopenfilename(
    #     initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

    # def return_home(self):
    # self.controller.show_frame("StartPage")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    root.destroy()  # optional; see description below
