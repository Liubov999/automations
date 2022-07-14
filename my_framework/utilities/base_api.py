from my_framework.api_collections import config
import requests


class BaseAPI:

    def __init__(self):
        self.base_url = config.config['base_url']
        self.request = requests
        self.headers = {}

    def get(self, url, body=None, headers=None, params=None):
        print('GET from BaseAPI')
        if headers is None:
            headers = self.headers
        response = self.request.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        print(f'Perform GET request')
        return response
