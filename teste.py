import tkinter as tk

# Importando a classe CampoHarmonicoMaior e CampoHarmonicoMenor
from main import CampoHarmonicoMaior, CampoHarmonicoMenor

# Função a ser chamada quando um botão é clicado
def botao_clicado(nota):
    label.config(text=f"Tom {nota} selecionado!")

# Função a ser chamada quando o botão de campo harmônico é clicado
def campo_harmonico_clicado():
    tonica = label.cget("text").split()[1]  # Obtendo o tom selecionado
    # Verificando se é maior ou menor
    if tonica[-1] == 'm':
        campo_harmonico = CampoHarmonicoMenor(tonica)
    else:
        campo_harmonico = CampoHarmonicoMaior(tonica)
    # Exibindo os acordes correspondentes na interface
    acordes_label.config(text="Campo Harmônico:")
    for acorde, notas in campo_harmonico.acordes.items():
        acordes_label.config(text=acordes_label.cget("text") + f"\n{acorde}: {'-'.join(notas)}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Piano Virtual")

# Criando um rótulo para exibir a mensagem do tom selecionado
label = tk.Label(janela, text="Selecione um tom")
label.pack(pady=10)

# Criando um frame para conter os botões das notas naturais e sustenidos
frame_botoes_naturais = tk.Frame(janela)
frame_botoes_naturais.pack()

# Criando um frame para conter os botões das notas menores
frame_botoes_menores = tk.Frame(janela)
frame_botoes_menores.pack()

# Notas de um piano
notas_piano_naturais = ["C", "D", "E", "F", "G", "A", "B"]
notas_piano_sustenidos = ["C#", "D#", "F#", "G#", "A#"]

# Criando os botões para as notas naturais e empacotando-os no frame horizontalmente
for nota in notas_piano_naturais:
    botao = tk.Button(frame_botoes_naturais, text=nota, command=lambda nota=nota: botao_clicado(nota))
    botao.pack(side=tk.LEFT, padx=5, pady=5)

# Criando os botões para as notas sustenidas e empacotando-os no frame horizontalmente
for nota in notas_piano_sustenidos:
    botao = tk.Button(frame_botoes_naturais, text=nota, command=lambda nota=nota: botao_clicado(nota))
    botao.pack(side=tk.LEFT, padx=5, pady=5)

# Notas menores de um piano
notas_piano_menores = ["Cm", "C#m", "Dm", "D#m", "Em", "Fm", "F#m", "Gm", "G#m", "Am", "A#m", "Bm"]

# Criando os botões para as notas menores e empacotando-os no frame horizontalmente
for nota in notas_piano_menores:
    botao = tk.Button(frame_botoes_menores, text=nota, command=lambda nota=nota: botao_clicado(nota))
    botao.pack(side=tk.LEFT, padx=5, pady=5)

# Criando um botão para mostrar o campo harmônico
botao_campo_harmonico = tk.Button(janela, text="Mostrar Campo Harmônico", command=campo_harmonico_clicado)
botao_campo_harmonico.pack(pady=10)

# Criando uma label para exibir os acordes do campo harmônico
acordes_label = tk.Label(janela, text="")
acordes_label.pack()

# Iniciando o loop principal da interface gráfica
janela.mainloop()
