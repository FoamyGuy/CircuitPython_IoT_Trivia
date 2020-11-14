# This code is a partial mod of of the Adafruit PyPotal lib
# https://github.com/adafruit/Adafruit_CircuitPython_PyPortal/blob/master/adafruit_pyportal.py


def wrap_nicely(string, max_chars):
    """Wrap nicely function

    A helper that will return a list of lines with word-break wrapping

    Parameters
    ----------
    string : str
        The text to be wrapped
    max_chars: int
        The maximum number of characters on a line before wrapping
    Returns
    -------
    list
        Returns a list of lines where each line is separated based
        on the amount of max_chars provided
    """
    string = string.replace('\n', '').replace('\r', '')  # Strip confusing newlines
    words = string.split(' ')
    the_lines = []
    the_line = ''
    for w in words:
        if len(the_line + ' ' + w) <= max_chars:
            the_line += ' ' + w
        else:
            the_lines.append(the_line)
            the_line = '' + w
    if the_line:  # Last line remaining
        the_lines.append(the_line)
    # Remove first space from first line:
    the_lines[0] = the_lines[0][1:]
    return the_lines