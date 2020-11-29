# import unittest
# unittest.main('test_call_wifi')


import unittest

from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import bitmap_label
import call_wifi


class TestCallWifi(unittest.TestCase):
    def test_call_wifi(self):
        """
        test call_wifi works properly
        """
        # Setup
        font = bitmap_font.load_font('SourceSansPro-Regular.bdf')
        output_label = bitmap_label.Label(font, color=0xFFFFFF, max_glyphs=30 * 4)
        output_label.line_spacing = 0.8
        output_label.anchor_point = (0, 0)
        output_label.anchored_position = (0, 0)

        # Calls
        error_check = call_wifi.call_wifi(output_label)
        
        # Asserts
        self.assertIsNone(error_check)
