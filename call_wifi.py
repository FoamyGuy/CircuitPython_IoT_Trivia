import ipaddress
import wifi
from secrets import secrets
from display_helpers import show_text


def call_wifi(label):
    """Wifi connect function

    Parameters
    ----------
    label : str
        Output label 

    Returns
    -------
    None
    """
    try:
        # Setup wifi and connection
        print(wifi.radio.connect(secrets['ssid'], secrets['password']))
        print('ip', wifi.radio.ipv4_address)
        show_text("ip: {}".format(wifi.radio.ipv4_address), label)
        ipv4 = ipaddress.ip_address('8.8.8.8')
        ping_result = wifi.radio.ping(ipv4)
        print('ping', ping_result)
        show_text("ping: {}".format(ping_result), label)
    except:
        return False
