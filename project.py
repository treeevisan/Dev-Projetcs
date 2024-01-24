import requests
from bs4 import BeautifulSoup
import re
import webbrowser as wb
import pyautogui as pyg
import time
import pandas as pd


def importar(caminho):
    global df

    df = pd.read_csv(caminho)
    df.reset_index
    return df



def concat(df):
    global dicio
    dicio = {}
    global url
    global a
    global c

    for i in range (len(df)):
        z = 'https://www.google.com/search?q='
        a = df.iloc[i][0]
        b = '+'
        c = df.iloc[i][1]
        url = z+a+b+c
        print('Pesquisando por: {}'.format(a+' '+c))
        abrir_aba(url)
        pesquisar(url)
        print('-'*20)
        time.sleep(0.5)
        fechar_nav()
        
    #fechar_nav()
        

def abrir_nav(url):
    wb.open_new(url)
    time.sleep(2)


def abrir_aba(url):
    wb.open_new(url)
    time.sleep(0.5)

def fechar_nav():
    pyg.hotkey('ctrl', 'w')


def pesquisar(url):
    link = str("'"+ url +"'")
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    requisicao = requests.get(url, headers=headers)


    site = BeautifulSoup(requisicao.text, 'html.parser')

    h3 = site.find_all(jsname='UWckNb', limit=5)
    #print(h3)
    
    lista = []

    for link in h3:
        i = a+' '+c
        lista.append(link['href'])
        dicio [i] = lista
    print(dicio)

def format_dataset(df, dicio):
    df2 = df
    df2['search'] = str(list(dicio.values())[0][0])

    for i in range(int(len((list(dicio.values()))))):
        df2.at[i,'search'] = str(list(dicio.values())[i])
   




importar('D:\Projetos Python\Dev-Projetcs\dataset_wbs.csv')
concat(df)
format_dataset(df,dicio)



# print(dicio.keys())
# print(len(list(dicio.values())))
# print(dicio.items())
display(df)
# print(list(dicio.values())[0][0])

# df2 = df
# df2['search'] = str(list(dicio.values())[0])

# display(df2)

# for i in range(int(len((list(dicio.values()))))):
#     df2.at[i,'search'] = str(list(dicio.values())[i])

# display(df2)

# print(type(int(len(list(dicio.values())))))