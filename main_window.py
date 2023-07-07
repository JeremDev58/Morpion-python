from tkinter import Tk, Frame
from frame_selection import FrameSelection


class MainWindow(Tk):
    def __init__(self, **kwargs):
        Tk.__init__(self, **kwargs)
        self.main_container = FrameSelection(self)
        self.main_container.pack(fill="both", expand=1)

    def switch_frame(self, frame: Frame) -> None:
        self.main_container.destroy()
        self.main_container = frame
        self.main_container.pack(fill="both", expand=1)