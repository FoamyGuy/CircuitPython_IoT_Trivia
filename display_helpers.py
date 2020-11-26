import time
import board
import busio
import displayio
import adafruit_displayio_ssd1306

class OLEDFeatherWing:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        print("after i2c")
        # Instantiate OLED object
        displayio.release_displays()
        self._display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
        print("after display bus")
        self.display = adafruit_displayio_ssd1306.SSD1306(self._display_bus, width=128, height=32, rotation=180)


def show_text(text, label):
    """Show text function
    Parameters
    ----------
    text : str
        Text to show
    label: label
        Label to put the text into
    Returns
    -------
    None
    """
    text = str(text)
    label.text = ' '
    label.text = text
    before = time.monotonic()
    while time.monotonic() < before + 0.2:
        # Waiting for screen to finish drawing
        pass

def display_answers(answers, current_selected_answer, label):
    """Display answers function

    Parameters
    ----------
    answers : list
        List of answers
    current_selected_answer: int
        Int of a specific answer

    Returns
    -------
    None
    """
    lines = answers.copy()
    lines[current_selected_answer] = '>{}'.format(lines[current_selected_answer])
    if current_selected_answer <= 1:
        show_text('\n'.join(lines), label)
    else:
        show_text('\n'.join(lines[1:]), label)

def replace_escape_codes(input_str):
    return input_str.replace("&quot;", '"').replace("&#039;", "'")
