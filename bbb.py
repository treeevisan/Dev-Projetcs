


import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=ceo+google'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    

requisicao = requests.get(url, headers=headers)

print(requisicao)
#print(requisicao.text)

site = BeautifulSoup(requisicao.text, 'html.parser')
#print(site.prettify())

# h3 = site.find_all('h3', limit = 5)

# print(h3)


# pesquisa2 = site.find_all(class_='qLRx3b tjvcx GvPZzd cHaqb', role='text', limit=1)
# print(len(pesquisa2))
# print(pesquisa2)


pesquisa3 = site.find_all(jsname='UWckNb', limit=5)
print(len(pesquisa3))
print(pesquisa3)
print(pesquisa3[0]['href'])

h4 = site.find_all(class_='LC20lb MBeuO DKV0Md', limit=5)
print(len(h4))
print(h4[1]['class'])




# h1 = site.find_all('a')
# print(h1[60].attrs)
# print(len(h1))
# print(h1)



import webbrowser

webbrowser.open_new('https://www.google.com/search?q=ceo+google')
# webbrowser.close