import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Práctica Git") [cite: 58, 66]
        self.turno = "X" [cite: 59]
        self.tablero = [""] * 9 [cite: 60]
        self.botones = [] [cite: 61]
        self.crear_interfaz() [cite: 62]

    def crear_interfaz(self):
        for i in range(9):
            boton = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                              command=lambda i=i: self.marcar_casilla(i)) [cite: 67, 68]
            boton.grid(row=i//3, column=i%3) [cite: 69]
            self.botones.append(boton) [cite: 69]

    def marcar_casilla(self, i):
        if self.tablero[i] == "": [cite: 71]
            self.tablero[i] = self.turno [cite: 72]
            self.botones[i].config(text=self.turno) [cite: 73]
            self.turno = "O" if self.turno == "X" else "X" [cite: 75]

if __name__ == "__main__":
    root = tk.Tk() [cite: 82]
    juego = TicTacToe(root) [cite: 83]
    root.mainloop() [cite: 84]