# import unittest
# unittest.main('test_display_helpers')


import unittest

from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import bitmap_label
import display_helpers


class TestDisplayHelpers(unittest.TestCase):
    def test_show_text(self):
        """
        test show_text works properly
        """
        # Setup
        font = bitmap_font.load_font('SourceSansPro-Regular.bdf')
        output_label = bitmap_label.Label(font, color=0xFFFFFF, max_glyphs=30 * 4)
        output_label.line_spacing = 0.8
        output_label.anchor_point = (0, 0)
        output_label.anchored_position = (0, 0)

        # Calls
        error_check = display_helpers.show_text('test', output_label)
        
        # Asserts
        self.assertIsNone(error_check)


    def test_display_answers(self):
        """
        test display_answers works properly
        """
        # Setup
        font = bitmap_font.load_font('SourceSansPro-Regular.bdf')
        output_label = bitmap_label.Label(font, color=0xFFFFFF, max_glyphs=30 * 4)
        output_label.line_spacing = 0.8
        output_label.anchor_point = (0, 0)
        output_label.anchored_position = (0, 0)
        answers = ['test1', 'test2', 'test3']
        current_selected_answer = 1

        # Calls 
        error_check = display_helpers.display_answers(answers, current_selected_answer, output_label)

        # Asserts
        self.assertIsNone(error_check)


    def test_replace_escape_codes(self):
        """
        test replace_escape_codes works properly
        """
        # Setup
        input_str = '&quot; test &#039; &amp;'

        # Calls
        formatted_input_str = display_helpers.replace_escape_codes(input_str)

        # Asserts
        self.assertEqual(formatted_input_str, '" test \' &')