# №2 №3 №5
import sys
import requests
from bs4 import BeautifulSoup

url = "https://www.cbr.ru/scripts/XML_daily.asp"
need_valute = input("Введите курс какой валюты хотите узнать, 1: ").upper()


def currency_rates(argv):
    r = requests.get(url).text
    date = r[r.find('Date=') + 6:r.find('Date=') + 16]
    date = date.split('.')

    soup = BeautifulSoup(r, 'lxml')
    list_1 = []
    list_2 = []

    quotes1 = soup.find_all('charcode')
    for quote1 in quotes1:
        list_1.append(quote1.text)

    quotes2 = soup.find_all('value')
    for quote2 in quotes2:
        n = str(quote2.text)
        masha = float(n.replace(',', '.'))
        list_2.append(masha)

    our_dict = dict((zip(list_1, list_2)))

    if need_valute in our_dict:
        our_result = our_dict[f'{need_valute}'], 'руб ' + "Дата:", date
        print(our_result)
    else:
        return None

    return None


if __name__ == '__main__':
    exit(currency_rates(sys.argv))
