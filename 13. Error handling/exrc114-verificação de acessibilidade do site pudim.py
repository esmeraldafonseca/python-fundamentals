import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessivel no momento!')

else:
    print('Consegui acessar')