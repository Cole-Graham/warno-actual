import random
import string
from uuid import uuid4


def generate_random_string(length=10):
	print(''.join(random.choice(string.ascii_uppercase) for j in range(length)))


for i in range(4):
	print(str(uuid4()))

for i in range(2):
	generate_random_string()
