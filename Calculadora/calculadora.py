import tkinter as tk #Importa a Biblioteca "tkinter" para a criação de interface

modo_escuro = False
n_numero = False
historico = []

#Função que é chamada quando um botão é clicado com o cursor
def clique(valor):
    global n_numero
    if n_numero or entrada.get() == "Erro": #Limpa o resultado ou o "Erro que estiver no display
        entrada.delete(0, tk.END)
        n_numero = False
    entrada.insert(tk.END, valor) #Insere o valor clicado    

#Função para realizar os calculos
def calculo():
    global n_numero
    expressao = entrada.get()
    try:
        resultado = eval(expressao) #avalia a expressão
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado)) #Exibe o resultado
        historico.append(f"{expressao} = {resultado}") #Adiciona a conta no histórico
        atualizar_historico()
    except Exception: #Se der erro
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro") # Exibe "erro"
    n_numero = True #Faz o próximo número substituir o resultado anterior   

#Função que limpa o campo de entrada
def limpar():
    entrada.delete(0, tk.END)

# Atualiza o historico (Mostra os ultimos 5 calculos realizados)
def atualizar_historico():
    historico_texto.config(state='normal')
    historico_texto.delete("1.0", tk.END)
    for linha in historico[-5:]:
        historico_texto.insert(tk.END, linha + "\n")
    historico_texto.config(state='disabled') #Impede a edição pelo usuario

#Função para que o teclado possa ser utilizado
def tecla(event):
    tecla = event.char
    if tecla in "0123456789+-*/().": #Define as teclas que podem ser utilizadas
        clique(tecla) # Se for um dos caracteres permitidos, simula um clique
    elif tecla == "=" or event.keysym == "Return":
        calculo() #Executa o caulculo se pressionar "=" ou "Enter"
    elif event.keysym == "BackSpace":
        entrada.delete(len(entrada.get()) - 1, tk.END) #limpa o campo de entrada

#Função para alternar entre o modo claro e o escuro
def alternar_modo():
    global modo_escuro
    modo_escuro = not modo_escuro
    cor_bg = "#2b2b2b" if modo_escuro else "#ffffff"
    cor_fg = "#ffffff" if modo_escuro else "#000000"

    # Atualiza as cores dos elementos
    entrada.config(bg=cor_bg, fg=cor_fg)
    historico_texto.config(bg=cor_bg, fg=cor_fg)
    janela.config(bg=cor_bg)
    for botao in botoes_widgets:
        botao.config(bg=cor_bg, fg=cor_fg, activebackground=cor_bg, activeforeground=cor_fg)
    botao_modo.config(bg=cor_bg, fg=cor_fg)    

#Cria a janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x500")
janela.bind("<Key>", tecla) # Ativa as teclas do teclado à função 'tecla'

#Campo de entrada onde fica o cálculo
entrada = tk.Entry(janela, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entrada.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Lista dos botões
botoes = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", "C", "=", "+"),
    ("(", ")", ".")
]

botoes_widgets = []

# Cria os botões na janela
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

# Botão para alternar o modo escuro e claro
botao_modo = tk.Button(janela, text="Alternar tema", font=("Arial", 10), command=alternar_modo)
botao_modo.pack(pady=5)

#Rotulo "Histórico
tk.Label(janela, text="Histórico", font=("Arial", 12)).pack()

#Campo que exibe o histórico
historico_texto = tk.Text(janela, height=5, font=("Courier New", 10), state='disabled')
historico_texto.pack(fill="both", padx=10, pady=5)

# inicia a interface
janela.mainloop()    
