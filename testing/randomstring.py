import random
import string
import uuid


def generate_random_string(length=10):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))  # noqa


print(generate_random_string())
print(generate_random_string(), '\n')

print(generate_random_string())
print(generate_random_string(), '\n')

print(generate_random_string())
print(generate_random_string())


def generate_guid():
    return str(uuid.uuid4())


print('1')
print(f'"GUID": "{generate_guid()}",')
print(f'        "GroupeCombatGUID": "{generate_guid()}",')
print('2')
print(f'"GUID": "{generate_guid()}",')
print(f'        "GroupeCombatGUID": "{generate_guid()}",')
print('3')
print(f'"GUID": "{generate_guid()}",')
print(f'        "GroupeCombatGUID": "{generate_guid()}",')
print('4')
print(f'"GUID": "{generate_guid()}",')
print(f'        "GroupeCombatGUID": "{generate_guid()}",')
print('5')
print(f'"GUID": "{generate_guid()}",')
print(f'        "GroupeCombatGUID": "{generate_guid()}",')
print('6')
print(f'"GUID": "{generate_guid()}",')
print(f'        "GroupeCombatGUID": "{generate_guid()}",')

print('1')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('2')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('3')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('4')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('5')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('6')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('7')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('8')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('9')
print(f'        "CadavreGUID": "{generate_guid()}",')
print('10')
print(f'        "CadavreGUID": "{generate_guid()}",')
