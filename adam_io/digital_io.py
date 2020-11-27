"""
Digital Input/Output
============================
Use this class to create the arguments to pass into the ADAM object
"""
from xml.etree import ElementTree
from typing import List, Optional


class DigitalOutput:
    """
    Digital Output class to send as a request to ADAM
    If the same object is going to be used, do not forget to clear the object after each use
    otherwise, might send stale data to

    - initialize with a quantity, the default is 6 which is the number of digital outputs 6050D has
    - fill in as required
    - get in the dict form to send in the POST body

    """

    def __init__(self, quantity: int = 6, array: List[int] = None):
        """
        :param quantity: number of digital outputs
        :param array: pass in an array with the same size as quantity to initialize the internal
            digital output dictionary in an ordered manner. If the sizes mismatch, throws an exception
        """
        self._do = {f"DO{index}": None for index in range(0, quantity + 1)}
        if array:
            if len(array) != quantity:
                raise Exception("quantity and initial array sizes are different for digital output")
            self.array(array)

    def __setitem__(self, do_id: int, value: int):
        if type(value) is not int:
            raise TypeError("digital output only accepts integer 0 or 1")
        if type(do_id) is not int:
            raise TypeError("digital output id should be integer")
        self._do[f"DO{do_id}"] = value

    def array(self, array: List[Optional[int]]):
        """
        :param array: set the values of the internal digital output dictionary to the input array
        """
        for index, value in enumerate(array):
            self._do[f"DO{index}"] = value

    def clear(self):
        """
        clears the values of the internal digital output dictionary
        """
        self.array([None] * len(self._do))

    def as_dict(self):
        """
        same as __call__
        :return: the data ready to be sent over to ADAM
        """
        return {k: v for k, v in self._do.items() if v}

    def __call__(self):
        """
        same as as_dict
        :return: the data ready to be sent over to ADAM
        """
        return {k: v for k, v in self._do.items() if v}

    def __getitem__(self, do_id):
        return self._do[do_id]

    def __iter__(self):
        yield from self._do.items()

    def __str__(self):
        return '\n'.join([f"DO[{index}]={v}" for index, v in enumerate(self._do.values())])

    def __repr__(self):
        return '\n'.join([f"DO[{index}]={v}" for index, v in enumerate(self._do.values())])


class DigitalInput:
    """
    Digital Input class to be received from ADAM

    initialize it with the xml string then use it like a read-only list;
    d = DigitalInput(xml_str)
    d[0] === DI0
    d[1] === DI1
    ...  === ...
    ...  === ...
    ...  === ...
    d[11] === DI11

    """

    def __init__(self, xml_string: str):
        """
        :param xml_string: response string from ADAM
        """
        root = ElementTree.fromstring(xml_string)
        self.name = root.tag
        status = root.attrib['status']
        if status != 'OK':
            raise Exception("something wrong with the response, status is:", status)

        # convert xml to dictionary
        values = [int(di_element.text) for di in root for di_element in di if di_element.tag == "VALUE"]
        keys = ["DI" + di_element.text for di in root for di_element in di if di_element.tag == "ID"]
        self._di = dict(zip(keys, values))

    def __getitem__(self, di_id: int):
        if type(di_id) != int:
            raise TypeError("digital input id should be integer")
        return self._di[f"DI{di_id}"]

    def __iter__(self):
        yield from self._di.items()

    def __str__(self):
        return '\n'.join([f"DI[{index}]={v}" for index, v in enumerate(self._di.values())])

    def __repr__(self):
        return '\n'.join([f"DI[{index}]={v}" for index, v in enumerate(self._di.values())])
