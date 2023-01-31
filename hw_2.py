import requests
from pprint import pprint
import json


TOKEN =
class YaMyloader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
                }

    #
    def get_file_list(self):
        file_list_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(file_list_url,headers=headers)
        return response.json()


    def get_create_folder(self,path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        response = requests.put(f'{folder_url}/?path={path}',headers=headers)


    def _link_load_file(self,disk_file_path):
        """получаем ссылку на загрузку файла"""
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(link_url, headers=headers, params=params)
        return response.json()


    def load_file(self,disk_file_path,file_name):
        result = self._link_load_file(disk_file_path=disk_file_path)
        url = result.get('href')
        response = requests.put(url, data=open(file_name,'rb'))
        response.raise_for_status()
        if response.raise_for_status() == 201:
            print('victory!!!')



if __name__ == '__main__':

    ya = YaMyloader(token=TOKEN)
    ya.load_file(disk_file_path='test1/test23.txt',file_name='все получилось.txt')

