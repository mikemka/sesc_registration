import time
from random import choice
from string import ascii_lowercase as LETTERS_LOWER, digits as DIGITS, ascii_uppercase as LETTERS_UPPER


STEP = 5


def generate_id():
    r = hex(int(str(time.time() // 1)[-3::-1]))[3:] + choice(LETTERS_LOWER + DIGITS) + choice(LETTERS_LOWER + DIGITS)
    return '-'.join(r[i:i + STEP] for i in range(0, len(r), STEP))[::-1]
