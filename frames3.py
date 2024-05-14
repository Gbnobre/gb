from tkinter import *
class MinhaGUI:
 def __init__(self):

# Criando janelas
  self.janela1 = Tk()
  self.janela2 = Tk()
    
# Bandeira da França
  self.frame1 = Frame(self.janela1, bg='blue', height=200, width=80)
  self.frame2 = Frame(self.janela1, bg='white', heigth=200, width=80)
  self.frame3 = Frame(self.janela1, bg='red', height=200, width=80)
  self.frame1.pack(side='left')
  self.frame2.pack(side='left')
  self.frame3.pack(side='left')
    
# Bandeira da Holanda

  self.fram1 = Frame(self.janela2, bg='red', height=80, width=200)
  self.fram2 = Frame(self.janela2, bg= 'white', height=80, width=200)
  self.fram3 = Frame(self.janela2, bg= 'blue', height=80, width=200)
  self.fram1.pack(side='top')
  self.fram2.pack(side='top')
  self.fram3.pack(side='top')
    
# Fazer o Tkinter exibir o looping da janela
  mainloop()
minha_gui = MinhaGUI() 