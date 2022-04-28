import time
from random import choice
from string import ascii_lowercase as LETTERS_LOWER, digits as DIGITS


def generate_id(STEP=5):
    r = hex(int(str(time.time() // 1)[-3::-1]))[3:] + choice(LETTERS_LOWER + DIGITS) + choice(LETTERS_LOWER + DIGITS)
    return '-'.join(r[i:i + STEP] for i in range(0, len(r), STEP))[::-1]
