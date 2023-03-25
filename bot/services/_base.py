import json

import requests

from settings import API_URL
from ._exceptions import ApiRequestFailed


class BaseApiService:
    @classmethod
    def _request_api(cls, endpoint: str, data: dict) -> dict:
        try:
            response = requests.post(API_URL + endpoint, json=data)
            if response.status_code == 400:
                raise ApiRequestFailed
            return json.loads(response.text)
        except Exception as e:
            print(e)
            raise ApiRequestFailed
