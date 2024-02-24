#!
from datetime import datetime
import geocoder
import requests
import re


class Weather_data_com_cep:

    def __init__(self, cep, language='en'):
        self.cep = self.valida_cep(str(cep))
        self.momento_atual_do_user = datetime.today()
        self.determina_localizacao_user = geocoder.osm(self.cep)
        self.lat, self.long = self.pega_coordenadas_user()
        self.url = self.pega_a_url(language)
        self.horario_certo = self.formata_data()

    def formata_data(self):
        data_formatada = self.momento_atual_do_user.strftime("Dia: %d/%m/%y e Horario: %H:%M")
        return data_formatada

    def __str__(self):
        return self.formata_data()

    def valida_cep(self, cep):
        if len(cep) == 8 or len(cep) == 5:
            # Cep brasileiro
            padrao_cep_br = re.compile(r'(\d){5}(\d){3}')
            match = padrao_cep_br.match(cep)
            # Cep americano
            padrao_cep_eua = re.compile(r'(\d){5}')
            match = padrao_cep_eua.match(cep)
            if match:
                return cep
        raise ValueError("CEP inválido")

    def pega_a_url(self, language):
        API_key = '871fe94c5e1d369ebb37f3b8589c8ac8'
        url = (
            f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.long}&appid={API_key}&lang={language}')
        return url

    def pega_coordenadas_user(self):
        return self.determina_localizacao_user.latlng

    def pega_estado_user(self):
        return self.determina_localizacao_user.state

    def pega_cidade_user(self):
        if (self.determina_localizacao_user.city is None):
            self.determina_localizacao_user.city = ' '
        return self.determina_localizacao_user.city

    def faz_a_busca(self, url):
        busca = requests.get(url)
        busca_direcionada = busca.json()
        descricao = busca_direcionada['weather'][0]['description']
        temperatura = busca_direcionada['main']['temp'] - 273.15
        max_temp = busca_direcionada['main']['temp_max'] - 273.15
        umidade = busca_direcionada['main']['humidity']
        vento = busca_direcionada['wind']['speed']
        return (
            f'clima: {descricao}, temp: {temperatura:.2f}ºC, humidade do ar: {umidade}%, no {self.horario_certo} em {self.pega_cidade_user()}, {self.pega_estado_user()}')

    def faz_a_busca_dentro_da_url(self):
        resultado = self.faz_a_busca(self.url)
        return resultado


if __name__ == "__main__":
    cep = 10001
    w = Weather_data_com_cep(cep)
    print(w.faz_a_busca_dentro_da_url())
