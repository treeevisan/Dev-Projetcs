

import requests
from bs4 import BeautifulSoup
import re



with open('Pagina Hashtag.html', 'r', encoding='utf-8') as arquivo:

    site = BeautifulSoup(arquivo, 'html.parser')

print(site.prettify())

titulo = site.title

#Elemento titulo

print(titulo)

#Texto do titulo
print(titulo.text)

#Elemento h1

h1 = site.find('h1')

print(h1)
print(h1.text)


#Elemento barra de navegação

barra_nav = site.find('nav')
print(barra_nav)

#Procurando dentro do elemento

#find retorna o primeiro elemento

link = barra_nav.find('a')
print(link)


#findall retorna TODOS os elementos em LISTA

links = barra_nav.find_all('a')
print(links)
print(links[0])


#Explorando os atributos (dicionario)

print(links[0].attrs)

#Escolhendo o atributo que você quer exatamente

print(links[0]['href'])


for link in links:
    print(link['href'])



#Encontrando elementos com varias regras
    
element_nav = barra_nav.find_all(['a','button'])
print(len(element_nav))


#Buscando por classe --> Tem que passar com '_' 
# por ser palavra reservada do python >> class = class_

titulo = site.find(class_ = 'tit')
print(titulo)

#É possivel pesquisar por mais de um atributo a mesma coisa

header = site.find(id = 'header')
print(header)

header2 = site.find(role = 'banner')
print(header2)

header3 = site.find(id = 'header', role = 'banner')
print(header3)

#Buscando com atributos

logo = site.find('img')
print(logo)

#Atributo com hifen precisa ser passado em forma de dicionário

logo = site.find('img',{'data-ll-status': 'loaded'})
print(logo)

#--------------- // -----------------------// ----------------------


#Buscando por texto

#Texto é igual

foco_mercado = site.find(text = 'Foco no Mercado')

print(foco_mercado)

foco_mercado = site.find(string = 'Foco no Mercado')

print(foco_mercado)


# Importar biblioteca "re" (regular expressions)
# Busca por textos que contenham alguma palavra

import re

textos = site.find_all(string = re.compile('alunos'))
print(textos)


# Parent e Contents

#Ver o elemento que contem o texto, ou onde ele está contido
# Importante para extrair outras caracteristicas do texto

# A cada .parent ele vai subindo na identação do texto

parent = textos[0].parent
print(parent)

parent = textos[0].parent.parent
print(parent)

# Printa todos os elementos de um texto / atributo

print(barra_nav.contents)

for elemento in barra_nav:
    print(elemento)


print(barra_nav.contents[1].contents)

titulo_alunos = site.find(id=re.compile('mais-de-'))
print(titulo_alunos)

print(titulo_alunos.contents)

print(titulo_alunos.contents[0].contents)