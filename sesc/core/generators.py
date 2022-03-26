import time
from random import choice
from string import ascii_lowercase as s1, digits as s2


def generate_id():
    r = hex(int(str(time.time() // 1)[-3::-1]))[3:] + choice(s1 + s2) + choice(s1 + s2)
    STEP = 5
    return '-'.join(r[i:i + STEP] for i in range(0, len(r), STEP))[::-1]
