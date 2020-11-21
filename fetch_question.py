import gc
import json
import ssl
import adafruit_requests
import time
import socketpool
import wifi
from call_wifi import call_wifi
from display_helpers import show_text


# Init request object
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Question URL
QUESTION_URL = 'https://opentdb.com/api.php?amount=1&type=multiple'


def fetch_question(label):
    """Display fetch_question function

    Parameters
    ----------
    None

    Returns
    -------
    Dict
        Response_obj dict
    """
    succeed = False
    while not succeed:
        # Garbage collect before our GET request
        gc.collect()
        # Perform a GET on the DATA_SOURCE and instantiate into a response object
        show_text('Fetching Question', label)
        print('Fetching Question')
        try:
            # Create our response and DATA objects
            response = requests.get(QUESTION_URL)
            response_obj = response.json()
            response.close()
            succeed = True
            return response_obj
        except OSError as e:
            print(e)
            show_text('OS Error. Retrying', label)
            time.sleep(2)

        # Garbage collect after our GET request
        gc.collect()
