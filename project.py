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
    global url
    for i in range (len(df)):
        z = 'https://www.google.com/search?q='
        a = df.iloc[i][0]
        b = '+'
        c = df.iloc[i][1]
        url = z+a+b+c
        abrir_aba(url)
        print('Pesquisando por: {}'.format(url))
        


def abrir_nav(url):
    wb.open_new(url)
    time.sleep(2)


def abrir_aba(url):
    wb.open_new(url)
    time.sleep(0.5)

def fechar_nav():
    pyg.hotkey('ctrl', 'w')


def pesquisar():
    pass
    time.sleep(3)



importar('D:\Projetos Python\Dev-Projetcs\dataset_wbs.csv')
concat(df)


