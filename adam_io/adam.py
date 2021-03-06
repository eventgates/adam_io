"""
ADAM 6050-D
===========
Main ADAM module to make the requests for input and output operations
"""

from xml.etree import ElementTree

from .digital_io import DigitalInput, DigitalOutput
from .requestor import Requestor
from .utils import valid_ipv4
from typing import Optional


class Adam6050D:
    """
    Only the ADAM6050D module is supported.
    """

    DO_COUNT = 6
    DI_COUNT = 12

    def __init__(self, ip: str, username: str, password: str):
        """
        Username and password should already be setup from APEX(?)
        :param ip: ip address of ADAM, should be of the form 0.0.0.0
        :param username: username for ADAM
        :param password: password for ADAM
        """
        if not valid_ipv4(ip):
            raise Exception("not a valid ip address ", ip)
        self.requestor = Requestor(ip, username, password)

        # make an initial request
        # input_response = self.input()
        # print("Initialized " + input_response.name)

    def output(self, digital_output: Optional[DigitalOutput] = None):
        """
        This prepares the data and sends it over to ADAM.

        :param digital_output: DigitalOutput, if the digital_output is None, read the values, not set them.
        :return: True for success, raises an exception if unsuccessful
        """

        # set the value(s) of the current state to that of input's
        if digital_output:
            current_state = self.requestor.output()
            current_do = DigitalOutput(xml_string=current_state)
            for key, val in digital_output:
                key = int(key.replace("DO", ""))
                if val is not None:
                    current_do[key] = digital_output[key]
            response = self.requestor.output(current_do.as_dict())
            root = ElementTree.fromstring(response)
            status = root.attrib['status']
            if status != "OK":
                raise Exception("Couldn't update output: ", status)
            return True
        else:
            response = self.requestor.output(digital_output)
            return DigitalOutput(xml_string=response)

    def input(self, digital_input_id: Optional[int] = None):

        """
        Read the values of the digital inputs

        :param digital_input_id: DIx if the digital_input_id is None, read the all values
        :return: ADAM response
        """
        response = self.requestor.input(digital_input_id)
        return DigitalInput(response)

    def on(self):
        """
        All digital outputs to HIGH
        """
        do = DigitalOutput(array=[1] * Adam6050D.DO_COUNT)
        # this is also acceptable
        # do.array([1, 1, 1, 1, 1, 1])
        # as well as this
        # do[0] = 1
        # do[1] = 1
        # do[2] = 1
        # do[3] = 1
        # do[4] = 1
        # do[5] = 1
        return self.output(do)

    def off(self):
        """
        All digital outputs to LOW
        """
        do = DigitalOutput(array=[0] * Adam6050D.DO_COUNT)
        return self.output(do)
