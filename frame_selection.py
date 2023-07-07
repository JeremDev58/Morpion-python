from tkinter import Frame, Label, StringVar, Button
from tkinter.ttk import Combobox
from game import Game


class FrameSelection(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.container = Frame(self)
        self.players = Label(self.container, text="Contre qui voulais vous jouer ?")
        self.mode = StringVar()
        self.values = ["X P1 --> AI O",
                       "O P1 --> AI X",
                       "X P1 --> P2 O",
                       "O P1 --> P2 X"]
        self.selector = Combobox(self.container, textvariable=self.mode, values=self.values)

        self.container.pack(fill="both")
        self.players.pack(side="left")
        self.selector.pack(side="left")

        self.container_command = Frame(self)
        self.btn_valid = Button(self.container_command, text="Valider", command=lambda: self.master.switch_frame(
            Game(self.master, self.values.index(str(self.mode.get())), (0, 0))))

        self.container_command.pack(side="bottom", fill="x")
        self.btn_valid.pack(side="right")



