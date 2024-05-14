# Como usar Frames em Python?

# Vamos fazer uma aplicação que vai exibir dois frames.
# Em cada um dos frames, vais colocar um Label, com um texto simples em cada um.
# Primeiro, damos um import em tudo (*) do módulo tkinter.
# Nossa classe que vai criar o programinha, se chama MinhaGUI.

# Primeiro, instanciamos o objeto da Tk(), que é nossa janela principal.
# Depois, vamos criar dois frames: o frame_cima e o frame_baixo, através da classe Frame(),
# que tem que recebe como argumento um objeto do tipo Tk(),
# no nosso caso é o objeto janela_principal, que é onde os frames estarão localizados (janela mãe).

# A seguir, criamos dois labels, o label1 e o label2, e passamos os frames criados como argumento, um label para cada frame.
# Damos o pack() pra posicionar os labels nos respectivos frames.
# E por fim, damos o pack() para posicionar os frames (sim, frames também precisam ser posicionados nas janelas).
# Depois é só chamar a função mainloop() que vai fazer sua aplicação rodar bonitinha.


from tkinter import *

class MinhaGUI:
 def __init__(self):
# Criando a janela principal
   self.janela_principal = Tk()

# Criando os frames
   self.frame_cima = Frame(self.janela_principal, bg= 'white', height=70, width=400)
   self.frame_baixo = Frame(self.janela_principal, bg= 'red', height=70, width=400)

# Criando os labels
   self.label1 = Label(self.frame_cima, text= 'Parte de cima do frame')
   self.label2 = Label(self.frame_baixo, text= 'Parte de baixo do frame')

# Posicionando os labels nos frames 
   self.label1.pack(side='top')
   self.label2.pack(side='top')
   
# Posicionando o frame
   self.frame_cima.pack()
   self.frame_baixo.pack()
   
# Fazer o tkinter exibir o looping da janela
   mainloop()
minha_gui = MinhaGUI()