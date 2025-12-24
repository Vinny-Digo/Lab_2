import re
import requests
import unittest
from unittest.mock import patch


#Функция поиска IPv4 через URL с Regex`ом
def URL_Regex(url):
    response = requests.get(url)
    if response.status_code == 200:
        tables = re.findall(r'<table\sclass="wp-block-table my-ip-table">.*?<\/table>',
                            response.text, flags=re.DOTALL)

        addresses = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\b',
                               tables[0], flags=re.DOTALL)
        return addresses

    else:
        print(f'Ошибка HTTP: {response.status_code}')
        return None

#Пример работы с URL-запросом
'''for adr in URL_Regex('https://itarticle.ru/ipv4-ipv6-network-tables/'):
    print(adr)'''