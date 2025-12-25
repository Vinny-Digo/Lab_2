import re
import requests
import unittest
from unittest.mock import patch


#Функция поиска IPv4 через URL с Regex`ом
def url_regex(url):
    response = requests.get(url)
    if response.status_code == 200:
        tables = re.findall(r'<table\sclass="wp-block-table my-ip-table">.*?</table>',
                            response.text, flags=re.DOTALL)

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

#Пример работы с URL-запросом
'''for adr in url_regex('https://itarticle.ru/ipv4-ipv6-network-tables/'):
    print(adr)'''