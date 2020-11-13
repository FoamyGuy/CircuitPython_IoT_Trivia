import gc
import ipaddress
import wifi
import ssl
import socketpool
import terminalio
import displayio
import busio as io
import adafruit_requests
import json
import digitalio
from wrap_nicely import wrap_nicely
import adafruit_displayio_ssd1306
import displayio
import busio
import board
import time
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from secrets import secrets


def display_answers(answers, current_selected_answer):
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
        display_text('\n'.join(lines))
    else:
        display_text('\n'.join(lines[1:]))


def scroll():
    """Scroll function

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    global _cur_scroll_index
    print(_cur_scroll_index)
    _cur_scroll_index += 1
    print(_cur_scroll_index)
    lines = output_label.text.split("\n")
    if _cur_scroll_index + LINES_VISIBLE > len(lines):
        _cur_scroll_index = 0
    display_text("\n".join(wrap_nicely(question_data['results'][0]['question'], 25)[_cur_scroll_index:]))


def display_text(text):
    """Display text function

    Parameters
    ----------
    text : str
        Text to print
    line: int
        Line to print text on

    Returns
    -------
    None
    """
    text = str(text)
    output_label.text = ' '
    output_label.text = text
    before = time.monotonic()
    while time.monotonic() < before + 0.2:
        # Waiting for screen to finish drawing
        pass


# Config
STATE_QUESTION = 0
STATE_ANSWER = 1
STATE_RESULT = 2
CUR_STATE = STATE_QUESTION
LINES_VISIBLE = 3
_cur_scroll_index = 0
current_selected_answer = 0
all_answers = []

# Instantiate i2c object
i2c = busio.I2C(board.SCL, board.SDA)

# Instantiate OLED object
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
font = bitmap_font.load_font('SourceSansPro-Regular.bdf')
output_label = label.Label(font, color=0xFFFFFF, max_glyphs=30 * 4)
output_label.line_spacing = 0.8
output_label.anchor_point = (0, 0)
output_label.anchored_position = (0, 0)
display_ssd1306 = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32, rotation=180)
display_ssd1306.show(output_label)

# Read trivia.json
f = open('trivia.json', 'r')
question_str = f.read()
f.close()
question_data = json.loads(question_str)
display_text('\n'.join(wrap_nicely(question_data['results'][0]['question'], 25)))

# Pins
c_pin = digitalio.DigitalInOut(board.IO33)
c_pin.direction = digitalio.Direction.INPUT
c_pin.pull = digitalio.Pull.UP
b_pin = digitalio.DigitalInOut(board.IO38)
b_pin.direction = digitalio.Direction.INPUT
b_pin.pull = digitalio.Pull.UP
a_pin = digitalio.DigitalInOut(board.IO1)
a_pin.direction = digitalio.Direction.INPUT
a_pin.pull = digitalio.Pull.UP
old_c_val = c_pin.value
old_b_val = b_pin.value
old_a_val = a_pin.value

while True:
    cur_c_val = c_pin.value
    if not cur_c_val and old_c_val:
        print('pressed c')
        if CUR_STATE == STATE_QUESTION:
            CUR_STATE = STATE_ANSWER
            all_answers = question_data['results'][0]['incorrect_answers']
            all_answers.append(question_data['results'][0]['correct_answer'])
            display_answers(all_answers, current_selected_answer)
        elif CUR_STATE == STATE_ANSWER:
            CUR_STATE = STATE_RESULT
            if all_answers[current_selected_answer] == question_data['results'][0]['correct_answer']:
                display_text('Correct! YaY')
            else:
                display_text('Incorrect')
        elif CUR_STATE == STATE_RESULT:
            CUR_STATE = STATE_QUESTION
            display_text('\n'.join(wrap_nicely(question_data['results'][0]['question'], 25)))
    old_c_val = cur_c_val

    cur_b_val = b_pin.value
    if not cur_b_val and old_b_val:
        print('pressed b')
    old_b_val = cur_b_val

    cur_a_val = a_pin.value
    if not cur_a_val and old_a_val:
        print('pressed a')
        if CUR_STATE == STATE_QUESTION:
            scroll()
        if CUR_STATE == STATE_ANSWER:
            current_selected_answer += 1
            if current_selected_answer > 3:
                current_selected_answer = 0
            display_answers(all_answers, current_selected_answer)
    old_a_val = cur_a_val

    time.sleep(0.05)
