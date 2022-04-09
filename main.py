import os
import requests
from pprint import pprint
from datetime import datetime
from datetime import timedelta


class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}


    def upload_link(self, path_on_yadisk: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        parameters = {"path": path_on_yadisk, "overwrite": "true"}
        order = requests.get(upload_url, headers=headers, params=parameters)
        return order.json()


    def upload(self, path_on_yadisk: str, file: str):
        path_json = self.upload_link(path_on_yadisk=path_on_yadisk)
        path = path_json['href']
        send = requests.put(path, data=open(file, 'rb'))
        send.raise_for_status()
        if send.status_code == 201:
             print(f'\nЗапись файла на Yandex Disk осуществлена успешно \n----------------------------------------'
                   '----------------------------------')
        # Функция может ничего не возвращать


def stack_over():
    questions = {}
    url = "https://api.stackexchange.com/2.3/questions?site=stackoverflow&tagged=python"
    questions_order = requests.get(url).json()['items']
    time = datetime.now() - timedelta(days=2)
    print(f'stackoverflow.com \nВопросы с тегом Python с {time} до текущего момента: \n')
    for quest in questions_order:
        date = datetime.fromtimestamp(quest['creation_date'])
        if time < date:
            date = date.isoformat(sep=' ')
            questions[date] = quest['title']
    return questions

if __name__ == '__main__':
    file = 'qwerty.txt'
    token = 'AQAAAAA5Ju1YAADLW-ELZgMfgEo6l_OWPBRKflo'
    path_to_file = os.path.abspath('qwerty.txt')
    path_on_yadisk = 'qwerty.txt'
    loader = YaUploader(token=token)
    loader.upload_link(path_on_yadisk)
    loader.upload(path_on_yadisk, path_to_file)
    pprint(stack_over())