import requests
import seaborn as sns


def plotar(titulo, labelx, labely, x, y, dataset, color):
    sns.set_palette('Accent')
    sns.set_style('darkgrid')
    ax = sns.lineplot(x=x, y=y, data=dataset)
    ax.figure.set_size_inches(14, 6)
    ax.set_title(titulo, loc='left', fontsize=18)
    ax.set_xlabel(labelx, fontsize=14)
    ax.set_ylabel(labely, fontsize=14)
    ax = sns.lineplot(x=x, y=y, data=dataset, color=color)
    ax = ax


def pegar_volatilidades():
    requesicao = requests.get('''
   http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,DOGE-BRL,ETH-BRL,LTC-BRL,JPY-BRL,CHF-BRL''')

    requesicao_dic = requesicao.json()

    # Moedas
    volatilidade_dolar = requesicao_dic['USDBRL']['pctChange']
    volatilidade_euro = requesicao_dic['EURBRL']['pctChange']
    volatilidade_iene = requesicao_dic['JPYBRL']['pctChange']
    volatilidade_suico = requesicao_dic['CHFBRL']['pctChange']

    # Criptos
    volatilidade_bitcoin = requesicao_dic['BTCBRL']['pctChange']
    volatilidade_dogecoin = requesicao_dic['DOGEBRL']['pctChange']
    volatilidade_ethereum = requesicao_dic['ETHBRL']['pctChange']
    volatilidade_litecoin = requesicao_dic['LTCBRL']['pctChange']

    volatilidade = [volatilidade_bitcoin, volatilidade_dogecoin, volatilidade_ethereum, volatilidade_litecoin,
                    volatilidade_dolar, volatilidade_euro, volatilidade_suico, volatilidade_iene]
    return volatilidade
