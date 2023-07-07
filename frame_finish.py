from tkinter import Frame, Label

from tkinter.font import Font


class FrameFinish(Frame):
    def __init__(self, master, terminus: int):
        Frame.__init__(self, master=master)
        self.font = Font(size=20)
        self.result = None
        if terminus == 2:
            self.result = Label(text="Match nul !", font=self.font)
        elif terminus == 1:
            self.result = Label(text="Le Joueur 2 remporte la partie !",font=self.font)
        else:
            self.result = Label(text="Le Joueur 1 remporte la partie !", font=self.font)
        self.result.pack(fill="both", expand=1)