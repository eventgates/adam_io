# check with status codes
# exceptions
# check 'error' and 'status'

from socket import inet_pton, inet_aton, AF_INET, error


def valid_ipv4(address: str):
    """
    :param address: ip address string
    :return: if the address is a valid dotted ipv4 address
    """
    try:
        inet_pton(AF_INET, address)
    except AttributeError:
        try:
            inet_aton(address)
        except error:
            return False
        return address.count('.') == 3
    except error:
        return False

    return True


class URI:
    DIGITAL_INPUT = "/digitalinput"
    DIGITAL_OUTPUT = "/digitaloutput"
    ALL = "/all"
    VALUE = "/value"
