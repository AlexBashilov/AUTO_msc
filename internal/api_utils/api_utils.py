import os

from httpx import Client


class ApiClient(Client):
    """
    Расширение стандартного клиента httpx.
    """

    def __init__(self):
        super().__init__(base_url=os.getenv('LOCALHOST'))
