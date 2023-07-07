from tkinter import Frame
from frame_score import FrameScore
from frame_game import FrameGame
from frame_command import FrameCommand
from frame_finish import FrameFinish
import time
import random


class Game(Frame):
    def __init__(self, master, mode: int, score: tuple):
        Frame.__init__(self, master)
        self.turn = "P1"
        self.rest_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.cur_player = "P1"
        self.players = {}
        self.ai = False
        self.winner = False
        if mode == 0:
            self.players.update({"P1": 'X', "P2": ["AI", "O"]})
            self.ai = True
        elif mode == 1:
            self.players.update({"P1": 'O', "P2": ["AI", "X"]})
            self.ai = True
        elif mode == 2:
            self.players.update({"P1": 'X', "P2": ["P2", "O"]})
        else:
            self.players.update({"P1": 'O', "P2": ["P2", "X"]})

        self.frame_game = FrameGame(self)
        self.frame_command = FrameCommand(self)

        self.frame_game.pack(fill="x")
        self.frame_command.pack(fill="x")


    def get_players(self):
        return self.players

    def get_cur_player(self):
        return self.cur_player

    def set_cur_player(self, cur: bool):
        if cur:
            self.cur_player = self.players["P2"][0]
        else:
            self.cur_player = "P1"

    def get_ai(self):
        return self.ai

    def ai_control(self):
        

        return

    def win_game(self):
        
        if self.winner:
            time.sleep(0.5)
            if self.cur_player != "P1":
                self.master.switch_frame(FrameFinish(self.master, 1))
            else:
                self.master.switch_frame(FrameFinish(self.master, 0))
        if len(self.rest_tiles) == 0:
            time.sleep(0.5)
            self.master.switch_frame(FrameFinish(self.master, 2))

    def find_tile_win(self, tile_cur):
        occur_find = tile_cur["text"]
        for i in range(0,8,3):
            if self.frame_game.tiles[i]["text"] == occur_find and \
                self.frame_game.tiles[i+1]["text"] == occur_find and \
                    self.frame_game.tiles[i+2]["text"] == occur_find :
                self.winner = True
        for i in range(3):
            if self.frame_game.tiles[i]["text"] == occur_find and \
                self.frame_game.tiles[i+3]["text"] == occur_find and \
                    self.frame_game.tiles[i+6]["text"] == occur_find :
                self.winner = True
        if self.frame_game.tiles[0]["text"] == occur_find and \
                self.frame_game.tiles[4]["text"]== occur_find and \
                    self.frame_game.tiles[8]["text"] == occur_find :
            self.winner = True
        if self.frame_game.tiles[2]["text"] == occur_find and \
                self.frame_game.tiles[4]["text"] == occur_find and \
                    self.frame_game.tiles[6]["text"] == occur_find :
            self.winner = True

    def next_player(self):
        if self.cur_player == "P1":
            self.lab_turn.configure(text="Au tour du joueur 1")
        else:
            self.lab_turn.configure(text="Au tour du joueur 2")
