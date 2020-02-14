import tkinter as tk 
from tkinter import ttk

def add():
    #lê o primeiro valor
    valor2 = valor.get()
    valor2 = float(valor2)
    print("valor2", valor2) #imprime o primeiro valor

    #lê o segundo valor
    valor4 = valor3.get()
    valor4 = float(valor4)
    print("segundo valor", valor4) #imprime o segundo valor
    
    #soma o segundo valor ao primeiro valor
    somatorio = valor2 + valor4
    print("Soma =", somatorio)
    
    #modifica a label mostra_resultado
    mostra_resultado.configure(text=somatorio)
#função que execulta a subtação 
def sub():
    #lê o primeiro valor
    valor2 = valor.get()
    valor2 = float(valor2)
    print("valor2", valor2) #imprime o primeiro valor

    #lê o segundo valor
    valor4 = valor3.get()
    valor4 = float(valor4)
    print("segundo valor", valor4) #imprime o segundo valor
    
    #soma o segundo valor ao primeiro valor
    subtrai = valor2 - valor4
    print("Soma =", subtrai)
    
    #modifica a label mostra_resultado
    mostra_resultado.configure(text=subtrai)    
    
win = tk.Tk()
   
   
win.title("Calculadora Simples")
#Cria a primeira label
label = ttk.Label(win, text="digite um numero")
label.grid(column=0, row=0)

#Cria a segunda label
label2 = ttk.Label(win, text="digite um numero")
label2.grid(column=0, row=1)

#Cria a label resultado
resultado_ = ttk.Label(win, text="Resultado")
resultado_.grid(column=0, row=2)

#Cria a label mostra_resultado
mostra_resultado = ttk.Label(win, text="=")
mostra_resultado.grid(column=1, row=2)

#Cria a primeira entrada
valor = ttk.Entry(win)
valor.grid(column=1, row=0)

#Cria a segunda entrada
valor3 = ttk.Entry(win)
valor3.grid(column=1, row=1)

#Botão de soma
soma = ttk.Button(win, text="+", command=add)
soma.grid(column=0, row=3)
#Botão de subtração
menos = ttk.Button(win, text="-", command=sub)
menos.grid(column=1, row=3)
#=====================
# Start GUI
#=====================
win.mainloop()