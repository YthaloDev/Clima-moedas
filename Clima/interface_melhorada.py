import customtkinter as ctk
from tkinter import *
from previsao_clima import *

# Setando a aparencia padrão do sistema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.all_system()

    def feedback_user(self, texto, x, y):
        lb_feedback = ctk.CTkLabel(self, text=f"{texto}", font=("Century Gothic bold", 16),
                                   text_color=('#000', '#fff'))
        lb_feedback.place(x=x, y=y)

    def layout_config(self):
        self.title('Sistema de Gestão de Cliente')
        self.geometry('600x400')

    def all_system(self):
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color='teal', fg_color='teal')
        frame.place(x=0, y=10)
        title = ctk.CTkLabel(frame, text="Previsor de Clima", font=("Century Gothic bold", 24),
                             text_color='#fff')
        title.place(x=205, y=10)

        def busca_cep():
            cep_variable = cep_value.get()
            if len(cep_variable) == 8 or len(cep_variable) == 5:
                # Cep brasileiro
                padrao_cep_br = re.compile(r'(\d){5}(\d){3}')
                match = padrao_cep_br.match(cep_variable)
                # Cep americano
                padrao_cep_eua = re.compile(r'(\d){5}')
                match = padrao_cep_eua.match(cep_variable)
                if match:
                    self.feedback_user('                      ', 240, 220)
                    cepvariable = cep_value.get()
                    # Chama a função do Clima
                    linguagem = "pt_br"
                    clima = Weather_data_com_cep(cepvariable, language=linguagem)
                    resultado_de_busca = clima.faz_a_busca_dentro_da_url()

                    output_text.delete(1.0, END)  # Limpa o conteúdo existente
                    output_text.insert(END, resultado_de_busca)
            else:
                self.feedback_user('CEP inválido!', 240, 220)

        # Labels
        lb_cep = ctk.CTkLabel(self, text='Digite o Cep do local', font=("Century Gothic bold", 16),
                              text_color=('#000', '#fff'))

        # Entry
        cep_value = StringVar()
        cep_entry = ctk.CTkEntry(self, width=270, font=("Century Gothic bold", 16), textvariable=cep_value,
                                 fg_color="transparent")

        # Button
        btn_busca_cep = ctk.CTkButton(self, text='Buscar'.upper(), command=busca_cep, fg_color='#555', hover_color='#333')
        btn_busca_cep.place(x=400, y=180)

        # Output Text
        output_text = ctk.CTkTextbox(self, width=500, height=100, font=("arial", 18), border_color='#aaa',
                                     border_width=2, fg_color='transparent')
        output_text.place(x=40, y=250)

        # Posições
        lb_cep.place(x=40, y=140)
        cep_entry.place(x=120, y=180)


if __name__ == '__main__':
    cadastro = App()
    cadastro.mainloop()
