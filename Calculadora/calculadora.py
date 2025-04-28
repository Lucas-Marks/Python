import tkinter as tk

modo_escuro = False
n_numero = False
historico = []

def clique(valor):
    global n_numero
    if n_numero or entrafa.get() == "Erro":
        entrada.delete(0, tk.END)
        n_numero = False
    entrada.insert(tk.END, valor)    


def calculo():
    global n_numero
    expressao = entrada.get()
    try:
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        historico.append(f"{expressao} = {resultado}")
        atualizar_historico()
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")
    n_numero = True    

def limpar():
    entrada.delete(0, tk.END)

def atualizar_historico():
    historico_texto.config(state='normal')
    historico_texto.delete("1.0", tk.END)
    for linha in historico[-5:]:
        historico_texto.insert(tk.END, linha + "\n")
    historico_texto.config(state='disabled')

def tecla(event):
    tecla = event.char
    if tecla in "0123456789+-*/().":
        clique(tecla)
    elif tecla == "=":
        calculo()
    elif event.keysym == "Return":
        calculo()
    elif event.keysym == "BackSpace":
        entrada.delete(len(entrada.get()) - 1, tk.END)

def alternar_modo():
    global modo_escuro
    modo_escuro = not modo_escuro
    cor_bg = "#2b2b2b" if modo_escuro else "#ffffff"
    cor_fg = "#ffffff" if modo_escuro else "#000000"
    entrada.config(bg=cor_bg, fg=cor_fg)
    historico_texto.config(bg=cor_bg, fg=cor_fg)
    janela.config(bg=cor_bg)
    for botao in botoes_widgets:
        botao.config(bg=cor_bg, fg=cor_fg, activebackground=cor_bg, activeforeground=cor_fg)
    botao_modo.config(bg=cor_bg, fg=cor_fg)    

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x500")
janela.bind("<Key>", tecla)

entrada = tk.Entry(janela, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entrada.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

botoes = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", "C", "=", "+"),
    ("(", ")", ".")
]

botoes_widgets = []

for linha in botoes:
    frame = tk.Frame(janela)
    frame.pack(expand=True, fill="both")
    for texto in linha:
        if texto == "=":
            botao = tk.Button(frame, text=texto, font=("Arial", 18), command=calculo)
        elif texto == "C":
            botao = tk.Button(frame, text=texto, font=("Arial", 18), command=limpar)
        else:
            botao = tk.Button(frame, text=texto, font=("Arial", 18), command=lambda v=texto: clique(v))
        botao.pack(side="left", expand=True, fill="both")
        botoes_widgets.append(botao)

botao_modo = tk.Button(janela, text="Alternar tema", font=("Arial", 10), command=alternar_modo)
botao_modo.pack(pady=5)

tk.Label(janela, text="Histórico", font=("Arial", 12)).pack()
historico_texto = tk.Text(janela, height=5, font=("Courier New", 10), state='disabled')
historico_texto.pack(fill="both", padx=10, pady=5)

janela.mainloop()    
