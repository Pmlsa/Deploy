import requests
import username
import urllib.parse
from bs4 import BeautifulSoup

class MinuteInbox:

    def __init__(self):
        self.API_URL = "https://www.minuteinbox.com"

        self.email_endpoint = "/email/id/2"
        self.refresh_endpoint = "/index/refresh"
        self.delete_endpoint = "/delete"

        self.session = requests.session()

        self.session.headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.minuteinbox.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }

    def generate_email(self):
        response = self.session.get(self.API_URL)
        soup = BeautifulSoup(response.text, "html.parser" )
        email = soup.find("span", {"id": "email"}).string
        return email

    def refresh_email(self, email):
        cookies = {
            'MI': urllib.parse.quote_plus(email),
        }

        response = self.session.get(self.API_URL + self.refresh_endpoint, cookies=cookies)
        return response.text

    def get_email(self, email):
        cookies = {
            'MI': urllib.parse.quote_plus(email),
        }
        response = self.session.get(self.API_URL + self.email_endpoint, cookies=cookies)
        return response.text

mail = MinuteInbox()
print(mail.get_email("karden.eon@sellcow.net"))