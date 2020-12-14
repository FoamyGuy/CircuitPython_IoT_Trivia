# import unittest
# unittest.main('test_fetch_question')


import unittest
import gc
import random

import displayio
import digitalio
import board
import time
from call_wifi import call_wifi
from fetch_question import fetch_question
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import bitmap_label
from display_helpers import OLEDFeatherWing, show_text, display_answers, replace_escape_codes
import fetch_question


class TestFetchQuestion(unittest.TestCase):
    def test_fetch_question(self):
        """
        test fetch_question works properly
        """
        # Setup
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
        print('inital wifi')
        call_wifi(output_label)

        # Calls
        response_obj = fetch_question.fetch_question(output_label)

        # Asserts
        self.assertIsNotNone(response_obj)

        