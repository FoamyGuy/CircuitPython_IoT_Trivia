import gc
import random

import displayio
import digitalio
import board
import time
from call_wifi import call_wifi
from fetch_question import fetch_question
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import bitmap_label, wrap_text_to_lines
from display_helpers import OLEDFeatherWing, show_text, display_answers, replace_escape_codes

# Config
CUR_QUESTION_OBJ = None
STATE_QUESTION = 0
STATE_ANSWER = 1
STATE_RESULT = 2
CUR_STATE = STATE_QUESTION
current_selected_answer = 0
all_answers = []
score = 0
font = bitmap_font.load_font('SourceSansPro-Regular.bdf')
LINES_VISIBLE = 3
_cur_scroll_index = 0
output_label = bitmap_label.Label(font, color=0xFFFFFF, max_glyphs=30 * 4)
output_label.line_spacing = 0.8
output_label.anchor_point = (0, 0)
output_label.anchored_position = (0, 0)
oled_featherwing = OLEDFeatherWing()
oled_featherwing.display.show(output_label)

# Attempt to connect on boot
print('inital wifi')
call_wifi(output_label)

# Read trivia.json - if you wanted to try do build a db locally
# here is an example for you
# f = open('trivia.json', 'r')
# question_str = f.read()
# f.close()
# question_data = json.loads(question_str)
# display_text('\n'.join(wrap_nicely(CUR_QUESTION_OBJ['results'][0]['question'], 25)))

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

_question_text = None
print('going to loop')
while True:
    try:
        if CUR_QUESTION_OBJ is None:
            CUR_QUESTION_OBJ = fetch_question(output_label)
            # print(CUR_QUESTION_OBJ)
            _question_text = replace_escape_codes(CUR_QUESTION_OBJ['results'][0]['question'])

            show_text('\n'.join(wrap_text_to_lines(_question_text, 25)), output_label)

        cur_c_val = c_pin.value
        if not cur_c_val and old_c_val:
            # print('pressed c')
            if CUR_STATE == STATE_QUESTION:
                CUR_STATE = STATE_ANSWER
                all_answers = CUR_QUESTION_OBJ['results'][0]['incorrect_answers']
                all_answers.insert(random.randint(0, 3), CUR_QUESTION_OBJ['results'][0]['correct_answer'])
                display_answers(all_answers, current_selected_answer, output_label)
            elif CUR_STATE == STATE_ANSWER:
                CUR_STATE = STATE_RESULT
                if all_answers[current_selected_answer] == CUR_QUESTION_OBJ['results'][0]['correct_answer']:
                    score += 1
                    show_text('Correct! YaY\nScore: {}'.format(score), output_label)
                else:
                    show_text('Incorrect', output_label)
            elif CUR_STATE == STATE_RESULT:
                CUR_STATE = STATE_QUESTION
                CUR_QUESTION_OBJ = None  # Clear the question obj to fetch a new one
                current_selected_answer = 0  # Clear selected answer index
                _cur_scroll_index = 0  # Clear question scroll index
        old_c_val = cur_c_val

        cur_b_val = b_pin.value
        # if not cur_b_val and old_b_val:
            # print('pressed b')
        old_b_val = cur_b_val

        cur_a_val = a_pin.value
        if not cur_a_val and old_a_val:
            # print('pressed a')
            if CUR_STATE == STATE_QUESTION:
                # print(_cur_scroll_index)
                _cur_scroll_index += 1
                # print(_cur_scroll_index)
                lines = output_label.text.split('\n')
                # print('there are {} lines. cur index {}'.format(len(lines), _cur_scroll_index))
                if _cur_scroll_index + LINES_VISIBLE > len(lines):
                    _cur_scroll_index = 0
                show_text("\n".join(wrap_text_to_lines(_question_text, 25)[_cur_scroll_index:]), output_label)
            if CUR_STATE == STATE_ANSWER:
                current_selected_answer += 1
                if current_selected_answer > 3:
                    current_selected_answer = 0
                display_answers(all_answers, current_selected_answer, output_label)
        old_a_val = cur_a_val

        time.sleep(0.05)
    except RuntimeError as e:
        print(e)
        print('wait retry')
        time.sleep(5)
        call_wifi(output_label)
