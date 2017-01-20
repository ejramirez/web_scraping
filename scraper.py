import urllib2
from bs4 import BeautifulSoup

ob_page = 'http://banksandbeals.com/ob070929.html'

page = urllib2.urlopen(ob_page)

soup = BeautifulSoup(page, 'html.parser')

ob_box = soup.find('blockquote').find_all(['p', 'br', 'span', 'a'])

for ob in ob_box:
    obit = ob.text.strip()
    print obit.encode('utf-8')
