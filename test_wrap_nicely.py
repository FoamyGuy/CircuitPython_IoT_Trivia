# import unittest
# unittest.main('test_wrap_nicely')


import unittest

import wrap_nicely


class TestWrapNicely(unittest.TestCase):
    def test_wrap_nicely(self):
        """
        test text wraps properly
        """
        # Setup
        string = 'A string of text to test to see if it wraps nicely'
        max_chars = 10

        # Calls
        the_lines = wrap_nicely.wrap_nicely(string, max_chars)

        # Asserts
        self.assertEqual(the_lines, [
            'A string', 
            'of text to', 
            'test to', 
            'see if it', 
            'wraps', 
            'nicely'
        ])
