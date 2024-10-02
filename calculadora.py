import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk, ImageSequence
import pygame

def calcular_faltas(carga_horaria):
    total_aulas = carga_horaria * 60 // 45  
    frequencia_minima = total_aulas * 0.75  
    faltas_permitidas = total_aulas - frequencia_minima  
    return total_aulas, frequencia_minima, faltas_permitidas

def parar_musica():
    pygame.mixer.music.stop()

def resultado_aprovado(total_aulas, frequencia_minima, faltas_permitidas, faltas):
    resultado_janela = tk.Toplevel()
    resultado_janela.title("Resultado - Aprovado")

    imagem = Image.open('liberado.jpg')
    imagem = imagem.resize((400, 400), Image.LANCZOS)
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = tk.Label(resultado_janela, image=imagem_tk)
    label_imagem.image = imagem_tk
    label_imagem.pack(pady=10)

    faltas_restantes = faltas_permitidas - faltas

    if faltas_restantes == 1:
        texto_faltas = f"Você ainda pode faltar 1 vez."
    else:
        texto_faltas = f"Você ainda pode faltar {faltas_restantes:.0f} vezes."

    texto_resultado = (
        f"Total de aulas: {total_aulas}\n"
        f"Frequência mínima: {frequencia_minima:.0f} aulas\n"
        f"Faltas permitidas: {faltas_permitidas:.0f} faltas\n"
        f"{texto_faltas}"
    )

    label_texto = tk.Label(resultado_janela, text=texto_resultado, font=font_padrao)
    label_texto.pack(pady=10)

    pygame.mixer.init()
    pygame.mixer.music.load('plin.mp3')
    pygame.mixer.music.play(loops=-1)

    resultado_janela.protocol("WM_DELETE_WINDOW", lambda: [parar_musica(), resultado_janela.destroy()])

def play_gif(label, frames, index=0, delay=100):
    frame = frames[index]
    label.configure(image=frame)
    index = (index + 1) % len(frames)
    label.after(delay, play_gif, label, frames, index)

def resultado_reprovado():
    resultado_janela = tk.Toplevel()
    resultado_janela.title("Resultado - Reprovado")

    gif_image = Image.open('rep.gif')
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif_image)]

    label_gif = tk.Label(resultado_janela)
    label_gif.pack(pady=10)

    play_gif(label_gif, frames)

    label_texto = tk.Label(resultado_janela, text="Reprovado por falta", font=font_padrao)
    label_texto.pack(pady=10)

    pygame.mixer.init()
    pygame.mixer.music.load('plon.mp3')
    pygame.mixer.music.play(loops=-1)

    resultado_janela.protocol("WM_DELETE_WINDOW", lambda: [parar_musica(), resultado_janela.destroy()])

def calcular():
    try:
        faltas = int(entry_faltas.get())
        total_aulas, frequencia_minima, faltas_permitidas = calcular_faltas(carga_horaria_atual)

        if faltas > faltas_permitidas:
            resultado_reprovado()
        else:
            resultado_aprovado(total_aulas, frequencia_minima, faltas_permitidas, faltas)

    except ValueError:
        messagebox.showwarning("Entrada inválida", "Por favor, insira um número válido de faltas.")

def set_carga_horaria(carga_horaria):
    global carga_horaria_atual
    carga_horaria_atual = carga_horaria
    label_carga_horaria.config(text=f"Carga Horária: {carga_horaria} horas")
    
    label_faltas.grid(row=3, column=0, pady=10, sticky="ew")
    entry_faltas.grid(row=4, column=0, pady=5, sticky="ew")
    botao_calcular.grid(row=5, column=0, pady=20, sticky="ew")

def estilo_botao(botao):
    botao.config(bg="#4CAF50", fg="white", font=font_padrao, bd=0, relief="flat")
    botao.bind("<Enter>", lambda e: botao.config(bg="#45a049"))
    botao.bind("<Leave>", lambda e: botao.config(bg="#4CAF50"))

janela = tk.Tk()
janela.title("Calculadora de Faltas")

font_padrao = font.Font(size=16)

frame = tk.Frame(janela)
frame.pack(expand=True)

frame.columnconfigure(0, weight=1)

botao_30h = tk.Button(frame, text="30 horas", command=lambda: set_carga_horaria(30))
estilo_botao(botao_30h)
botao_30h.grid(row=0, column=0, pady=5, sticky="ew")

botao_60h = tk.Button(frame, text="60 horas", command=lambda: set_carga_horaria(60))
estilo_botao(botao_60h)
botao_60h.grid(row=1, column=0, pady=5, sticky="ew")

botao_90h = tk.Button(frame, text="90 horas", command=lambda: set_carga_horaria(90))
estilo_botao(botao_90h)
botao_90h.grid(row=2, column=0, pady=5, sticky="ew")

label_carga_horaria = tk.Label(frame, text="Selecione uma carga horária", font=font_padrao)
label_carga_horaria.grid(row=6, column=0, pady=10)

label_faltas = tk.Label(frame, text="Digite o número de faltas:", font=font_padrao)
entry_faltas = tk.Entry(frame, font=font_padrao)

botao_calcular = tk.Button(frame, text="Calcular", command=calcular)
estilo_botao(botao_calcular)
botao_calcular.grid(row=5, column=0, pady=20, sticky="ew")

janela.update_idletasks()
largura = 400
altura = 300
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f'{largura}x{altura}+{x}+{y}')

janela.mainloop()
