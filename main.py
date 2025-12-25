import re
import requests
import unittest
from unittest.mock import patch


#Функция поиска IPv4 через Input с Regex`ом
def user_input_regex():
    while True:
        quantity = int(input('Введите количество IP-адресов, которые хотели бы проверить : '))
        if bool((re.match(r'[\d]+', str(quantity)))):
            for i in range(quantity):
                data = str(input('Введите IP-адрес : '))
                if bool((re.match(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\b', data))):
                    print('Данный IP-адрес корректен !')
                    continue
                else:
                    print('Данный IP-адрес некорректен !')
                    continue
            break
        else:
            print('Введите число корректно !')
            continue

#Функция поиска IPv4 через URL с Regex`ом
def url_regex(url):
    data = requests.get(url)
    if data.status_code == 200:
        tables = re.findall(r'<table\sclass="wp-block-table my-ip-table">.*?</table>',
                            data.text, flags=re.DOTALL)

        addresses = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\b',
                               tables[0], flags=re.DOTALL)
                                                #255 - 250      249 - 200       199 - 100   99 - 0
        return addresses

    else:
        return None

#Класс unitest`а
'''class TestURLRegex(unittest.TestCase):

    @patch('requests.get')
    def test_url_regex_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<table class="wp-block-table my-ip-table">255.255.255.255</table>'
        expected_ip = ['255.255.255.255']

        result = url_regex('https://itarticle.ru/ipv4-ipv6-network-tables/')
        
        self.assertEqual(result, expected_ip)
        mock_get.assert_called_once_with('https://itarticle.ru/ipv4-ipv6-network-tables/')

    @patch('requests.get')
    def test_url_regex_failure(self, mock):
        mock.return_value.status_code = 404

        result = url_regex('https://itarticle.ru/ipv4-ipv6-network-tables/')

        self.assertIsNone(result)'''

def MAIN():
    print('=' * 35)
    print(' Проверка корректности IP-адресов !')
    print('=' * 35, '\n')

    while True:
        print('1. Пользовательский ввод')
        print('2. Проверка по URL','\n')
        choice = str(input('Ваш выбор : '))
        if (choice == '1') or (choice == '2'):
            choice = int(choice)
            match choice:
                case 1:
                    user_input_regex()
                    break
                case 2:
                    print('Для проверки работоспособности кода был использован ресурс :','https://itarticle.ru/ipv4-ipv6-network-tables/','\n')
                    input('Нажмите Enter, чтобы продолжить \n')
                    print('Найденные IP-адреса :')
                    for adr in (url_regex('https://itarticle.ru/ipv4-ipv6-network-tables/')):
                        print(adr)
                    break
        else:
            print('Введите число корректно !','\n')
            continue

MAIN()