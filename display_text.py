from display_text import display_text


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
