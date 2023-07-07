from tkinter import Frame, Button, Label
from tkinter.font import Font
import random
import time



class FrameGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.font = Font(size=18)
        self.fg = "#f34e5c"
        self.bg = "#383836"
        self.winner = 0
        self.lab_turn = Label(self,text="Au tour du joueur 1")
        self.lab_turn.pack(fill="x")
        self.container_tiles = Frame(self)
        self.container_tiles.pack(fill="x")
        self.tiles = []
        for i in range(3):
            for j in range(3):
                btn = Button(self.container_tiles, height=5, width=5, bg=self.bg, font=self.font)
                btn.bind("<Button-1>", self.tiles_select)
                btn.grid(column=i, row=j)
                self.tiles.append(btn)
                btn.setvar()

    def tiles_select(self, evt):
        ref = self.tiles.index(evt.widget)
        if self.tiles[ref]["state"] != "disabled": 
            if self.master.get_cur_player() == "P1":
                self.tiles[ref]["text"] = self.master.get_players()["P1"]
                self.tiles[ref]["fg"] = "red"
                self.find_tile_win(evt.widget)
                self.tiles[ref]["state"] = "disabled"
                self.master.rest_tiles.remove(self.tiles.index(evt.widget))
                self.switch_label_turn()
                self.master.win_game()
                self.master.set_cur_player(False)
                if self.master.ai:
                    self.tiles_ai_select()
            else:
                self.tiles[ref]["text"] = self.master.get_players()["P2"][1]
                self.tiles[ref]["fg"] = "green"
                self.find_tile_win(evt.widget)
                self.tiles[ref]["state"] = "disabled"
                self.master.rest_tiles.remove(self.tiles.index(evt.widget))
                self.switch_label_turn()
                self.master.win_game()
                self.master.set_cur_player(True)
        

    def tiles_ai_select(self, reroll=False):
        if not reroll:
            time.sleep(0.4)
        choice = random.randint(0, len(self.master.rest_tiles))
        btn = self.tiles[choice]
        btn["text"] = self.master.get_players()["P2"][1]
        btn["fg"] = "green"
        self.find_tile_win(btn)
        btn["state"] = "disabled"
        try:
            self.master.rest_tiles.remove(self.tiles.index(btn))
            self.switch_label_turn()
            self.master.win_game()
            self.master.set_cur_player(True)
        except:
            self.tiles_ai_select(True)

    def get_winner(self):
        return self.winner

    def get_tiles(self):
        return self.tiles
    
    def switch_label_turn(self):
        if self.master.cur_player == "P1":
            self.lab_turn.configure(text="Au tour du joueur 1")
        else:
            self.lab_turn.configure(text="Au tour du joueur 2")

    def find_tile_win(self, tile_cur):
        occur_find = tile_cur["text"]
        for i in range(0,8,3):
            if self.tiles[i]["text"] == occur_find and \
                self.tiles[i+1]["text"] == occur_find and \
                    self.tiles[i+2]["text"] == occur_find :
                self.master.winner = True
        for i in range(3):
            if self.tiles[i]["text"] == occur_find and \
                self.tiles[i+3]["text"] == occur_find and \
                    self.tiles[i+6]["text"] == occur_find :
                self.master.winner = True
        if self.tiles[0]["text"] == occur_find and \
                self.tiles[4]["text"]== occur_find and \
                    self.tiles[8]["text"] == occur_find :
            self.master.winner = True
        if self.tiles[2]["text"] == occur_find and \
                self.tiles[4]["text"] == occur_find and \
                    self.tiles[6]["text"] == occur_find :
            self.master.winner = True
