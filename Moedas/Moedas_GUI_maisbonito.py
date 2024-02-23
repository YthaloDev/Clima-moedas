import customtkinter as ctk
from tkinter import *
import pandas as pd
from Valor_moedas import *
from matplotlib import pyplot as plt

# Setando a aparencia padrão do sistema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

Volatilidade = pegar_volatilidades()
Criptos = ['Bitcoin', 'Dogecoin', 'Ethereum', 'Litecoin']
Moedas = ['Dólar', 'Euro', 'Franco Suiço', 'Iene']
criptos_vol = Volatilidade[:4]
moedas_vol = Volatilidade[4:]

# Tabelas com as minhas moedas
Moedas_fiduciarias = pd.DataFrame({'Fiduciárias': Moedas, 'Volatilidade': moedas_vol})
Cripto_moedas = pd.DataFrame({'Criptos': Criptos, 'Volatilidade': criptos_vol})


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.all_system()
        self.lb_try = None

    def layout_config(self):
        self.title('Sistema de Gestão de Cliente')
        self.geometry('600x400')

    def all_system(self):
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color='teal', fg_color='teal')
        frame.place(x=0, y=10)
        title = ctk.CTkLabel(frame, text="Moedas do Mercado", font=("Century Gothic bold", 24),
                             text_color='#fff')
        title.place(x=190, y=10)

        def search():
            coin = coin_value.get()
            if coin not in Criptos and coin not in Moedas:
                opcoes = ', '.join(Criptos + Moedas)
                lb_try = ctk.CTkLabel(self, text=f"Tente: {opcoes}", font=("Century Gothic bold", 14),
                                      text_color=('#000', '#fff'))
                lb_try.place(x=40, y=210)
            else:
                for moeda, vol in zip(Moedas_fiduciarias['Fiduciárias'], Moedas_fiduciarias['Volatilidade']):
                    if coin == moeda:
                        coin1 = ctk.CTkLabel(self, text=f"Volatilidade do {moeda} é {vol}               ",
                                             font=("Century Gothic bold", 14), text_color=('#000', '#fff'))
                        coin1.place(x=40, y=240)

                for cripto, vol in zip(Cripto_moedas['Criptos'], Cripto_moedas['Volatilidade']):
                    if coin == cripto:
                        coin2 = ctk.CTkLabel(self, text=f"Volatilidade do {cripto} é {vol}              ",
                                             font=("Century Gothic bold", 14), text_color=('#000', '#fff'))
                        coin2.place(x=40, y=240)
                        break

        def coins():
            plotar('Volatilidade Criptos', 'Criptos', 'Volatilidade', Criptos, criptos_vol, Cripto_moedas, 'purple')
            plt.show()

        def cryptos():
            plotar('Volatilidade Fiduciárias', 'Moedas', 'Volatilidade', Moedas, moedas_vol, Moedas_fiduciarias, 'red')
            plt.show()

        # Label
        lb_moeda = ctk.CTkLabel(self, text="Digite qual moeda gostaria de saber a volatibilidade",
                                font=("Century Gothic bold", 16), text_color=('#000', '#fff'))

        # Entry
        coin_value = StringVar()
        coin_entry = ctk.CTkEntry(self, width=290, font=("Century Gothic bold", 16), textvariable=coin_value,
                                  fg_color="transparent")

        # Butão
        btn_search = ctk.CTkButton(self, text='Buscar'.upper(), command=search, fg_color='#555', hover_color='#333')
        btn_search.place(x=420, y=180)

        btn_graphic_coin = ctk.CTkButton(self, text='Gráfico Moeda'.upper(), command=coins, fg_color='#151', hover_color='#131')
        btn_graphic_coin.place(x=40, y=280)

        btn_graphic_crypto = ctk.CTkButton(self, text='Gráfico Crypto'.upper(), command=cryptos, fg_color='#151', hover_color='#131')
        btn_graphic_crypto.place(x=268, y=280)

        # Posição
        lb_moeda.place(x=40, y=140)
        coin_entry.place(x=120, y=180)


if __name__ == '__main__':
    cadastro = App()
    cadastro.mainloop()
