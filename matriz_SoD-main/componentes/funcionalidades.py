from customtkinter import *
from componentes.func_btns import *


class Funcionalidades(CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.legenda_cadastros = CTkLabel(self, text="Cadastros", font=("sans-serif", 18))
      self.legenda_cadastros.grid(row=0, column=0, padx=30, pady=(60, 0))

      self.users = CTkButton(self, text="Usuários", command=self.user_window)
      self.users.grid(row=1, column=0, padx=30, pady=(25, 0), sticky="w")

      self.systems = CTkButton(self, text="Sistemas", command=self.sys_window)
      self.systems.grid(row=2, column=0, padx=30, pady=(25, 0), sticky="w")

      self.vizualizar = CTkLabel(self, text="Vizualizar", font=("sans-serif", 18))
      self.vizualizar.grid(row=3, column=0, padx=30, pady=(60, 0))

      self.matriz = CTkButton(self, text="Matriz")
      self.matriz.grid(row=4, column=0, padx=30, pady=(25, 20), sticky="w")

   def user_window(self):
      User(self.master)

   def sys_window(self):
      Systems(self)