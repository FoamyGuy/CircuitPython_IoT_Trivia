import ipaddress
import wifi
from secrets import secrets
from display_text import display_text


def call_wifi():
    """Wifi connect function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # Setup wifi and connection
    print(wifi.radio.connect(secrets['ssid'], secrets['password']))
    print('ip', wifi.radio.ipv4_address)
    display_text("ip: {}".format(wifi.radio.ipv4_address))
    ipv4 = ipaddress.ip_address('8.8.8.8')
    ping_result = wifi.radio.ping(ipv4)
    print('ping', ping_result)
    display_text("ping: {}".format(ping_result))
