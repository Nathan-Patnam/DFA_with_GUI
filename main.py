import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CreateDFA):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_title(controller)
        self.add_create_dfa_button(controller)

    def add_title(self, controller):
        label = tk.Label(self, text="PFLAP",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
    
    def add_create_dfa_button(self, controller):
        create_dfa = tk.Button(self, text="Create DFA",
                               command=lambda: controller.show_frame("CreateDFA"))
        create_dfa.pack()

class CreateDFA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_title(controller)
        self.add_upload_dfa_from_file_button()
        self.add_return_home_button()

    def add_title(self, controller):
        label = tk.Label(self, text="Create a DFA",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

    def add_upload_dfa_from_file_button(self):
        file_button = tk.Button(self, text="Create DFA from file",
                                command=self.ask_for_file)
        file_button.pack()

    def add_return_home_button(self):
        return_home_button = tk.Button(self, text="Go to the home page",
                           command=self.return_home)
        return_home_button.pack()

    def ask_for_file(self):
        root = tk.Tk()
        root.filename = filedialog.askopenfilename(
    initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
  

    def return_home(self):
        self.controller.show_frame("StartPage")
    



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
