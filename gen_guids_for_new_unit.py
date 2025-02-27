import random
import string
from uuid import uuid4

for i in range(4):
	print(str(uuid4()))

def generate_random_string(length=10):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))  # noqa

i = 2
while i > 0:
    print(generate_random_string())
    i -= 1
