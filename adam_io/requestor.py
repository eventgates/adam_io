import base64
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .digital_io import DigitalOutput
from .utils import URI


class Requestor:
    def __init__(self, ip: str, username: str, password: str):
        """
        For now no unauthorized requests are possible

        :param ip: ADAM ip
        :param username: ADAM username
        :param password: ADAM password
        """
        auth_str = f"{username}:{password}"
        encoded_auth_str = base64.b64encode(auth_str.encode('ascii')).decode('utf-8')
        self.headers = {"Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": "Basic " + encoded_auth_str}
        self.base_url = f"http://{ip}"

    def input(self, input_channel_id: int = None):
        """
        if the requests digital output index is out of bounds,
        request returns status code 501.

        :param input_channel_id: single input is requested, none returns all digital inputs
        :return: ADAM response
        """
        if input_channel_id:
            input_channel_id = "/" + str(input_channel_id)
            url = self.base_url + URI.DIGITAL_INPUT + input_channel_id + URI.VALUE
        else:
            url = self.base_url + URI.DIGITAL_INPUT + URI.ALL + URI.VALUE
        request = Request(url, headers=self.headers)
        response = urlopen(request)
        return response.read().decode('utf8')

    def output(self, data: DigitalOutput = None):
        """
        if the requests digital output index is out of bounds,
        request returns status code 501.

        :param data: DigitalOutput object
        :return: ADAM response
        """
        url = self.base_url + URI.DIGITAL_OUTPUT + URI.ALL + URI.VALUE

        if data:
            params = urlencode(data).encode('utf-8')
            request = Request(url, data=params, headers=self.headers)
        else:
            request = Request(url, headers=self.headers)

        response = urlopen(request)
        return response.read().decode('utf8')
