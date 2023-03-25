from ._types import OsiUser
from ._base import BaseApiService


class AuthService(BaseApiService):
    @classmethod
    def try_get_user(cls, iin: int, phone_number: str) -> OsiUser:
        input_data = {'iin': str(iin), 'telephone': phone_number}
        # user_info = requests.post(API_URL + 'user/get/info/', json=input_data)
        data = cls._request_api('user/get/info/', input_data)
        return OsiUser(
            iin=data['iin'],
            phone_number=data['telephone'],
            fullname=data['fullname']
        )
