import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Práctica Git")
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones = []
        self.crear_interfaz()

    def crear_interfaz(self):
        for i in range(9):
            boton = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                              command=lambda i=i: self.marcar_casilla(i))
            boton.grid(row=i//3, column=i%3)
            self.botones.append(boton)

    def marcar_casilla(self, i):
        if self.tablero[i] == "" and not self.verificar_ganador():
            self.tablero[i] = self.turno
            self.botones[i].config(text=self.turno)
            if self.verificar_ganador():
                messagebox.showinfo("Victoria", f"¡El jugador {self.turno} ha ganado!")
            elif "" not in self.tablero:
                messagebox.showinfo("Empate", "¡Es un empate!")
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        # Combinaciones para ganar: filas, columnas y diagonales 
        posiciones_victoria = [
            (0,1,2), (3,4,5), (6,7,8), # Filas
            (0,3,6), (1,4,7), (2,5,8), # Columnas
            (0,4,8), (2,4,6)           # Diagonales
        ]
        for a, b, c in posiciones_victoria:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != "":
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    juego = TicTacToe(root)
    root.mainloop()