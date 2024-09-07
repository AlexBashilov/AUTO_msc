import os

from httpx import Client, Response


class ApiClient(Client):
    """
    Расширение стандартного клиента httpx.
    """

    def __init__(self):
        super().__init__(base_url='https://tms-api-rest.intgr-test-' + os.getenv('STAGE') + '.ox1.dev/api')
