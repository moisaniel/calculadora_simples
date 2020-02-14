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

#função que execulta a Multiplicação 
def mult():
    #lê o primeiro valor
    valor2 = valor.get()
    valor2 = float(valor2)
    print("valor2", valor2) #imprime o primeiro valor

    #lê o segundo valor
    valor4 = valor3.get()
    valor4 = float(valor4)
    print("segundo valor", valor4) #imprime o segundo valor
    
    #soma o segundo valor ao primeiro valor
    vezes = valor2 * valor4
    print("Soma =", vezes)
    
    #modifica a label mostra_resultado
    mostra_resultado.configure(text=vezes)    

def div():
    #lê o primeiro valor
    valor2 = valor.get()
    valor2 = float(valor2)
    print("valor2", valor2) #imprime o primeiro valor

    #lê o segundo valor
    valor4 = valor3.get()
    valor4 = float(valor4)
    print("segundo valor", valor4) #imprime o segundo valor
    
    #soma o segundo valor ao primeiro valor
    dividir = valor2 / valor4
    print("Soma =", dividir)
    
    #modifica a label mostra_resultado
    mostra_resultado.configure(text=dividir)    
        
        
win = tk.Tk()
   
   
win.title("Calculadora Simples")
#Cria Frame 
frame2 = ttk.LabelFrame(win, text="botões teste2")
frame2.grid(column=0, row=1,  padx=20, pady=20)
#Cria a primeira label
label = ttk.Label(frame2, text="digite um numero", width=16)
label.grid(column=0, row=0, sticky=tk.W)

#Cria a segunda label
label2 = ttk.Label(frame2, text="digite um numero", width=16)
label2.grid(column=0, row=1, sticky=tk.W)

#Cria a label resultado
resultado_ = ttk.Label(frame2, text="Resultado", width=16)
resultado_.grid(column=0, row=2,sticky=tk.W)

#Cria a label mostra_resultado
mostra_resultado = ttk.Label(frame2, text="=")
mostra_resultado.grid(column=1, row=2, sticky=tk.W)

#Cria a primeira entrada
valor = ttk.Entry(frame2, width=16)
valor.grid(column=1, row=0, sticky=tk.W)

#Cria a segunda entrada
valor3 = ttk.Entry(frame2)
valor3.grid(column=1, row=1)
#Frame para botões
frame1 = ttk.LabelFrame(frame2, text="botões teste")
frame1.grid(column=0, row=3,  padx=20, pady=40)
#Botão de soma
soma = ttk.Button(frame1, text="+", command=add)
soma.grid(column=0, row=3, sticky=tk.W)
#Botão de subtração
menos = ttk.Button(frame1, text="-", command=sub)
menos.grid(column=1, row=3, sticky=tk.W)
#Botão multiplicar
multiplicar = ttk.Button(frame1, text="x", command=mult)
multiplicar.grid(column=2, row=3, sticky=tk.W)
#Botão divisão
_dividir = ttk.Button(frame1, text="/", command=div)
_dividir.grid(column=3, row=3, sticky=tk.W)
#=====================
# Start GUI
#=====================
win.mainloop()