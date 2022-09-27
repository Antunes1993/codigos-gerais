from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

'''
#Exercício 01 - Achando a primeira Tag de um determinado tipo. Foi também inserindo as rotinas de exceção para erros HTTP e URL
try: 
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print (e)
except URLError as e:
    print('O servidor não pode ser encontrado.')
else:
    bs = BeautifulSoup(html.read(), 'html5lib')
    print('Funcionou.')
    try: 
        badContent = bs.h1
    except AttributeError as e:
        print('Tag não encontrada 01.')
    else:
        if badContent == None: 
            print('Tag não encontrada 02.')
        else: 
            print(badContent)
'''
'''
#Exercício 02 - Encontra e lista todas as tags de um determinado tipo ('span').
#A partir dessa lista é feita uma verificação para achar todas as tags que tenham um determinado atributo (class:green).
try: 
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print (e)
except URLError as e:
    print('O servidor não pode ser encontrado.')
else:
    bs = BeautifulSoup(html.read(), 'html5lib')
    print('Funcionou.')
    nameList = bs.findAll('span',{'class':'green'})
    for name in nameList:
        print(name.get_text())
'''

'''
#Exercício 03 - Encontra e lista todas as tags de um determinado tipo ('span').
#A partir dessa lista é feita uma verificação para achar todas as tags que tenham um determinado atributo (class:green).
try: 
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print (e)
except URLError as e:
    print('O servidor não pode ser encontrado.')
else:
    bs = BeautifulSoup(html.read(), 'html5lib')
    print('Funcionou.')
    nameList = bs.findAll(text='the prince')
    print(len(nameList))
'''

'''
#Exercício 4 - Web Scrapping da webPage ilustrado na página 39.
try:
    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print ('O servidor não pode ser encontrado.')
else:
    bs = BeautifulSoup(html.read(), 'html5lib')
    
    tableContent = bs.find('table',{'id':'giftList'}).tr
    #print (tableContent.get_text())

    for image in bs.findAll('img',{'src':'../img/gifts/img1.jpg'}):
        print (image.parent.previous_sibling.get_text())
'''

'''
#Exercício 5 - Web Scrapping da webPage ilustrado na página 39 (mais elaborado).
try:
    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print ('O servidor não pode ser encontrado.')
else:
    bs = BeautifulSoup(html.read(), 'html5lib')
    images = bs.findAll('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
    lista_items = []
    for item in images:
        product = item.parent.previous_sibling.previous_sibling.previous_sibling.get_text()
        price = item.parent.previous_sibling.get_text()
        lista_items.append([product,price])
        #print("Produto: {} \n Preço {} ================".format(product, price))
    print (lista_items)
'''

#Exercício 6 - Six Degrees da Wikipedia
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html,'html5lib')
for link in bs.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])