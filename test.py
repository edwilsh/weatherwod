import requests
from bs4 import BeautifulSoup
import urllib3

xfit = requests.get('http://www.crossfitconditioning.com.au/wod.html')

wod = BeautifulSoup(xfit.text)

print(wod.table)
