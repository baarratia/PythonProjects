__author__ = 'Benja'
import re
import requests
import os

def Comprobar_Mensaje(Texto):
    x = re.search(r'(?<=\$\$)(.*?)(?=\$\$)', Texto)
    if x:
        return Buscar(x.group(0))
    else:
        return False, False

def Buscar(Pista):
    searchTerm = re.sub(' ', '%20', Pista)
    print(searchTerm)
    url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
       'v=1.0&q=' + searchTerm + '&as_filetype=jpg&start=10&rsz=1&imgsz=icon')
    response = requests.get(url)
    dic = dict(response.json())
    url = dic['responseData']['results'][0]['url']
    data = requests.get(url, stream=True)
    print(data.status_code)
    if data.status_code == 200:
        with open("Data/{}.png".format(searchTerm), 'wb') as f:
            f.write(data.content)
        return True, searchTerm
    else:
        return False, False