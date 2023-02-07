import urllib
import urllib.request

try:
    urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('Site não está acessível no momento.')
else:
    print('Enjoy!')